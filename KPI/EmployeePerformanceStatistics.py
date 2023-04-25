import os
import csv
import json
import yaml
import time
import requests
from math import log
from datetime import datetime
from cffi.backend_ctypes import long

base_url = "https://project.feishu.cn/"
project_key = "psp"
work_item_type_key = "issue"
routing = f"/open_api/{project_key}/work_items/{work_item_type_key}/search/params"

header = {
    "Content-Type": "application/json",
    "X-PLUGIN-TOKEN": "",
          }


class Operator:
    Reg = "~"                   # 匹配
    NReg = "!~"                 # 不匹配
    Eq = "="                    # 等于
    Ne = "!="                   # 不等于
    Lt = "<"                    # 小于
    Gt = ">"                    # 大于
    Lte = "<="                  # 小于等于
    Gte = ">="                  # 大于等于
    HasAnyOf = "HAS ANY OF"     # 存在选项属于
    HasNoneOf = "HAS NONE OF"   # 不存在选项属于
    IsNull = "IS NULL"          # 为空
    NotNull = "IS NOT NULL"     # 不为空


def str_to_timestamp(time_str):
    date_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return long(time.mktime(date_time.timetuple()) * 1000.0 + date_time.microsecond / 1000.0)


class FeishuAPI(object):
    plugin_token = None
    user_key = None
    users_name = []
    emails = []
    users_info = {}

    def __init__(self, user_key, plugin_id, plugin_secret, type):
        self.plugin_token = self.get_plugin_token(plugin_id, plugin_secret, type)
        self.user_key = user_key

    def get_plugin_token(self, plugin_id, plugin_secret, type):
        try:
            headers = {"Content-Type": "application/json"}
            plugin_token_routing = "/bff/v2/authen/plugin_token"
            url = base_url + plugin_token_routing
            request_body = {"plugin_id": plugin_id, "plugin_secret": plugin_secret, "type": type}
            r = requests.post(url, json=request_body, headers=headers)
            response_json = json.loads(r.content.decode("utf-8"))
            return response_json.get("data").get("token")
        except Exception as e:
            print(str(e))

    # 通过查询参数获取项目缺陷列表
    def get_project_issue_list_by_search_params(self, project_key, search_group, page_num, page_size=50,
                                                x_plugin_token='plugin_token'):
        result = []
        try:
            # 由于有分页限制，故需递归聚合每一页结果
            def do_search(page_num, page_size):
                get_work_item_by_search_params_routing = f'/open_api/{project_key}/work_item/issue/search/params'
                url = base_url + get_work_item_by_search_params_routing
                headers = {}
                if x_plugin_token == "plugin_token":
                    headers = {
                        "Content-Type": "application/json",
                        "X-PLUGIN-TOKEN": self.plugin_token,
                        "X-USER-KEY": self.user_key
                    }
                # 获取user_plugin_token流程较长，暂未实现
                elif x_plugin_token == "user_plugin_token":
                    headers = {
                        "Content-Type": "application/json"
                    }
                    pass
                request_body = {"page_size": page_size, "page_num": page_num, "search_group": search_group}
                r = requests.post(url, json=request_body, headers=headers)
                response_json = json.loads(r.content.decode("utf-8"))
                page_num = response_json.get("pagination").get("page_num")
                page_size = response_json.get("pagination").get("page_size")
                total = response_json.get("pagination").get("total")
                result.extend(response_json.get("data"))
                if total - page_num * page_size > 0:
                    do_search(page_num + 1, page_size)
            do_search(page_num + 1, page_size)
            return result
        except Exception as e:
            print((str(e)))

    # 获取在特定时间段内创建的项目缺陷列表
    def get_project_issue_by_created_time(self, project_key, lower_timestamp, upper_timestamp):
        lower = str_to_timestamp(lower_timestamp)
        upper = str_to_timestamp(upper_timestamp)
        search_group = {
            "conjunction": "AND",
            "search_params": [
                {
                    "param_key": "created_at",
                    "operator": ">=",
                    "value": lower
                },
                {
                    "param_key": "created_at",
                    "operator": "<=",
                    "value": upper
                }
            ]
        }
        return self.get_project_issue_list_by_search_params(project_key, search_group, 0)


    # 获取在特定时间段内创建并处于特定状态的项目缺陷列表
    def get_project_issue_in_specified_status_by_created_time(self, project_key, operator, status, lower_timestamp,
                                                              upper_timestamp):
        lower = str_to_timestamp(lower_timestamp)
        upper = str_to_timestamp(upper_timestamp)
        search_group = {
            "conjunction": "AND",
            "search_params": [
                {
                    "param_key": "created_at",
                    "operator": ">=",
                    "value": lower
                },
                {
                    "param_key": "created_at",
                    "operator": "<=",
                    "value": upper
                },
                {
                    "param_key": "work_item_status",
                    "operator": operator,
                    "value": status
                }
            ]
        }
        return self.get_project_issue_list_by_search_params(project_key, search_group, 0)

    '''未完成'''
    # 获取制定人员及时间段内的工作项列表
    def get_project_work_item_in_a_specific_person_and_update_time_period(self, project_key, user_keys,
                                                                          update_start_time, update_end_time, page_num,
                                                                          page_size=200, x_plugin_token='plugin_token'):
        get_specified_work_item_routing = f'open_api/{project_key}/work_item/filter'
        url = base_url + get_specified_work_item_routing
        if x_plugin_token == 'plugin_token':
            headers = {
                "Content-Type": "application/json",
                "X-PLUGIN-TOKEN": self.plugin_token,
                "X-USER-KEY": self.user_key
            }
        # 获取user_plugin_token流程较长，暂未实现
        elif x_plugin_token == "user_plugin_token":
            headers = {
                "Content-Type": "application/json"
            }
            pass
        start = str_to_timestamp(update_start_time + ' 00:00:00')
        end = str_to_timestamp(update_end_time + ' 23:59:59')
        request_body = {"work_item_type_keys": ["story"], "user_keys": user_keys, "updated_at": [start, end],
                        "page_size": page_size, "page_num": page_num}
        r = requests.post(url, json=request_body, headers=headers)
        response_json = json.loads(r.content.decode("utf-8"))
        print(response_json)
        return

    # 获取每人提交的缺陷列表
    def issue_group_by_creator(self, issue_list):
        issue_of_creator = {}
        if not issue_list:
            return None
        for issue in issue_list:
            creator = issue.get("created_by")
            if creator not in issue_of_creator.keys():
                issue_of_creator[creator] = []
            issue_of_creator[creator].append(issue)
        return issue_of_creator

    # 统计每人items梳理
    def count_items_number_of_each_person(self, items_of_owner):
        if not items_of_owner:
            return None
        count_result = {}
        for key, value in items_of_owner.items():
            count_result[key] = len(value)
        return count_result

    # 获取当前空间下用户姓名
    def get_users_chinese_name(self, user_keys=[], out_ids=[], emails=[], x_plugin_token="plugin_token"):
        try:
            headers = {}
            if x_plugin_token == "plugin_token":
                headers = {
                    "Content-Type": "application/json",
                    "X-PLUGIN-TOKEN": self.plugin_token,
                    "X-USER-KEY": self.user_key
                }
            # 获取user_plugin_token流程较长，暂未实现
            elif x_plugin_token == "user_plugin_token":
                headers = {
                    "Content-Type": "application/json"
                }
                pass
            query_user_routing = "/open_api/user/query"
            url = base_url + query_user_routing
            request_body = {"user_keys": user_keys, "out_ids": out_ids, "emails": emails}
            r = requests.post(url, json=request_body, headers=headers)
            response_json = json.loads(r.content.decode("utf-8"))
            users_info = {}
            for items in response_json.get("data"):
                if items['user_key'] not in users_info.keys():
                    users_info[items['user_key']] = items['name_cn']
            self.users_info = users_info
            return self.users_info
        except Exception as e:
            print(str(e))

    # 从yml导入配置信息
    def load_config_from_yaml(self, file_path='config.yml'):
        with open(file_path, encoding='utf8') as f:
            config = yaml.safe_load(f)
        f.close()
        return config

    # 根据姓名列表获取对应用户user_key
    def get_user_keys_by_name_list(self, name_list, users_info=None):
        if name_list is None:
            name_list = self.users_name
        if users_info is None:
            users_info = self.users_info
        res = {}
        for k, v in users_info.items():
            if v in name_list and v not in res.keys():
                res[v] = k
        return res

    # 统计给定项目下目标用户的提交及流转的缺陷数据
    def statistics_each_reporter_bugs(self, start_date, end_date, project_keys=None, names=None):
        statistics = {}
        # 加载配置信息
        config = self.load_config_from_yaml()
        # 要统计的项目project_key
        if not project_keys:
            project_keys = config.get('project_keys')
        # 要查询的用户姓名
        if not names:
            name_list = config.get('names')
        for project_key in project_keys:
            print(project_key)
            # 获取项目空间下指定时间段内创建的缺陷信息
            bugs = self.get_project_issue_by_created_time(project_key, start_date, end_date)
            # 目标时间段内未获取到bug，无需后续计算
            if bugs:
                # 根据缺陷创建人对缺陷信息分组
                each_person_bugs = self.issue_group_by_creator(bugs)
                # 统计每个缺陷创建人创建的缺陷数
                cnt = self.count_items_number_of_each_person(each_person_bugs)
                user_keys = []
                for k, v in cnt.items():
                    user_keys.append(k)
                # 获取指定user_key用户的姓名
                users_info = self.get_users_chinese_name(user_keys=user_keys)
                # 获取要查询的用户user_key
                users = self.get_user_keys_by_name_list(name_list, users_info)
                # 统计每人创建的bug数
                for name, user_key in users.items():
                    if user_key in cnt.keys():
                        if name not in statistics.keys():
                            statistics[name] = {}
                        if 'create_bugs' not in statistics[name].keys():
                            statistics[name]['create_bugs'] = cnt[user_key]
                        else:
                            statistics[name]['create_bugs'] += cnt[user_key]

            # 获取项目空间下指定时间段内非OPEN状态的缺陷信息
            non_open_bugs = self.get_project_issue_in_specified_status_by_created_time(project_key, Operator.Ne,
                                                                                       ['OPEN'], start_date, end_date)
            # 无非OPEN状态的bug，则无需后续计算
            if non_open_bugs:
                # 根据缺陷创建人对缺陷信息分组
                each_person_non_open_bugs = self.issue_group_by_creator(non_open_bugs)
            # 统计每个缺陷创建人下非OPEN状态的缺陷数
                cnt2 = self.count_items_number_of_each_person(each_person_non_open_bugs)
                user_keys = []
                for k, v in cnt2.items():
                    user_keys.append(k)
                    # 获取指定user_key用户的姓名
                users_info = self.get_users_chinese_name(user_keys=user_keys)
                # 获取要查询的用户user_key
                users = self.get_user_keys_by_name_list(name_list, users_info)
                # 统计每人创建的bug数
                for name, user_key in users.items():
                    if user_key in cnt2.keys():
                        if name not in statistics.keys():
                            statistics[name] = {}
                        if 'non_open_bugs' not in statistics[name].keys():
                            statistics[name]['non_open_bugs'] = cnt2[user_key]
                        else:
                            statistics[name]['non_open_bugs'] += cnt2[user_key]
            print(statistics)
        return statistics

    # 统计给定项目下包含目标用户估时或排期的需求卡片
    def statistics_estimated_duration_and_scheduling(self, start_date, end_date, project_keys=None, names=None):
        statistics = {}
        # 加载配置信息
        config = self.load_config_from_yaml()
        # 要统计的项目project_key
        if not project_keys:
            project_keys = config.get('project_keys')
        # 要查询的用户姓名
        if not names:
            name_list = config.get('names')
        for project_key in project_keys:
            print(project_key)


class PerformanceStatistics:
    def __init__(self, start_date, end_date):
        self.start_date = f'{start_date} 00:00:00'
        self.end_date = f'{end_date} 23:59:59'
        self.user_data = {}

    def get_user_data_by_date(self, start_date=None, end_date=None):
        if not start_date:
            start_date = self.start_date
        if not end_date:
            end_date = self.end_date
        api = FeishuAPI("7107077857691598851", "MII_6440B08E41848001", "443A864F59B968B821B43E599E57D860", 0)
        bugs = api.statistics_each_reporter_bugs(start_date, end_date)
        print(bugs)
        with open('config.yml', encoding='utf8') as f:
            config = yaml.safe_load(f)
        url = "https://main.lilithgames.com/api/testcase/statistic/count/history/user/PlatformTest"
        headers = {'content-type': 'application/json;charset=UTF-8', 'jwt': config['jwt']}
        payload = f'{{"projectId":"PlatformTest","emailList":[],"userGroupList":[2],"startTime":"{start_date}"' \
                  f',"endTime":"{end_date}"}}'
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.ConnectionError:
            print('网络异常')
        else:
            # try:
            user_data = []
            for k, v in response.json()['data'].items():
                create_bugs, non_open_bugs = 0, 0
                if bugs.get(k):
                    if bugs.get(k).get('create_bugs'):
                        create_bugs = bugs.get(k).get('create_bugs')
                    if bugs.get(k).get('non_open_bugs'):
                        non_open_bugs = bugs.get(k).get('non_open_bugs')
                open_bug_point = log(create_bugs - non_open_bugs, 42) if create_bugs - non_open_bugs > 0 else 0
                effective_bug_point = log(non_open_bugs, 42) if non_open_bugs > 0 else 0
                if k in config['names']:
                    case_increased_and_changed = v['testCaseNewCount'] + v['testCaseModifyCount']
                    case_maintenance_point = log(case_increased_and_changed, 370) if case_increased_and_changed > 0 else 0
                    case_execution_point = log(v['executionCaseExecuteCount'], 1700) if v['executionCaseExecuteCount'] > 0 else 0
                    user_data.append({'姓名': k,
                                      '新增用例数': v['testCaseNewCount'],
                                      '更新用例数': v['testCaseModifyCount'],
                                      '增改用例数': case_increased_and_changed,
                                      '用例维护分': case_maintenance_point,
                                      '执行用例数': v['executionCaseExecuteCount'],
                                      '用例执行分': case_execution_point,
                                      '提交缺陷数': create_bugs,
                                      '流转缺陷数': non_open_bugs,
                                      '非流转缺陷分': open_bug_point,
                                      '流转缺陷分': effective_bug_point,
                                      '基础产出分': case_maintenance_point * 20 + case_execution_point * 20 +
                                                     open_bug_point * 10 + effective_bug_point * 20
                                      })
            self.user_data = user_data
            print(user_data)
            return user_data
            # except:
            #     print('以下接口jwt token过期，请在config.yml中更新：\nhttps://main-test.lilithgames.com/api/testcase/statistic/count/history/user/PlatformTest')

    def get_user_data_by_date_from_xmind_platform(self, start_date=None, end_date=None):
        if not start_date:
            start_date = self.start_date
        if not end_date:
            end_date = self.end_date
        # 从飞书meego拉缺陷数据
        api = FeishuAPI("7107077857691598851", "MII_6440B08E41848001", "443A864F59B968B821B43E599E57D860", 0)
        bugs = api.statistics_each_reporter_bugs(start_date, end_date)
        print(bugs)

        # 从xmind用例管理平台拉用例数据
        with open('config.yml', encoding='utf8') as f:
            config = yaml.safe_load(f)
        emails = []
        names = []
        people = config.get("emails")
        for k, v in people.items():
            emails.append(k)
            names.append(v)
        url = "https://main.lilithgames.com/api/testcase-xmind/workload/type/statistic"
        headers = {'content-type': 'application/json'}
        user_data = []
        case_data = {}
        for data_type in ["new", "modify", "execute"]:
            e_mails = ''
            for e in emails:
                e_mails += f'"{e}",'
            payload = f'{{"emails":[{e_mails[:-1]}],"startDate":"{start_date}", "endDate":"{end_date}"' \
                      f', "projects":["PlatformTest"], "type":"{data_type}"}}'
            try:
                r = requests.request("POST", url, headers=headers, data=payload).json()
                if r['code'] == "24200" and r['data'] is not None:
                    for datum in r['data']:
                        if datum.get('email'):
                            if case_data.get(people[datum.get('email')]) is None:
                                case_data[people[datum.get('email')]] = {}
                            case_data[people[datum.get('email')]][data_type] = datum.get('count')
            except:
                pass
        for name, case in case_data.items():
            create_bugs, non_open_bugs = 0, 0
            if bugs.get(name):
                if bugs.get(name).get('create_bugs'):
                    create_bugs = bugs.get(name).get('create_bugs')
                if bugs.get(name).get('non_open_bugs'):
                    non_open_bugs = bugs.get(name).get('non_open_bugs')
            open_bug_point = log(create_bugs - non_open_bugs, 42) if create_bugs - non_open_bugs > 0 else 0
            effective_bug_point = log(non_open_bugs, 42) if non_open_bugs > 0 else 0
            if name in names:
                case_increased_and_changed = case['new'] + case['modify']
                case_maintenance_point = log(case_increased_and_changed, 370) if case_increased_and_changed > 0 else 0
                case_execution_point = log(case['execute'], 1700) if case['execute'] > 0 else 0
                user_data.append({'姓名': name,
                                  '新增用例数': case['new'],
                                  '更新用例数': case['modify'],
                                  '增改用例数': case_increased_and_changed,
                                  '用例维护分': case_maintenance_point,
                                  '执行用例数': case['execute'],
                                  '用例执行分': case_execution_point,
                                  '提交缺陷数': create_bugs,
                                  '流转缺陷数': non_open_bugs,
                                  '非流转缺陷分': open_bug_point,
                                  '流转缺陷分': effective_bug_point,
                                  '月提交缺陷分':effective_bug_point + open_bug_point,
                                  '基础产出分': case_maintenance_point * 20 + case_execution_point * 20 +
                                                open_bug_point * 10 + effective_bug_point * 20
                                  })
        self.user_data = user_data
        print(user_data)
        return user_data

    def create_csv(self, data=None):
        if not data:
            data = self.user_data
        file_path = os.path.split(os.path.realpath(__file__))[0] + f'/{self.start_date}~{self.end_date}.csv'
        if os.path.exists(file_path):
            os.remove(file_path)
        print(file_path)
        column_names = ['姓名', '新增用例数', '更新用例数', '增改用例数', '用例维护分', '执行用例数', '用例执行分', '提交缺陷数', '流转缺陷数','非流转缺陷分', '流转缺陷分', '基础产出分']
        try:
            with open(file_path, 'x', encoding="utf-8-sig", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=column_names)
                writer.writeheader()
                for datum in data:
                    writer.writerow(datum)
        except IOError:
            print("IO错误")
        finally:
            csv_file.close()

    def create_csv_for_xmind_platform(self, data=None):
        if not data:
            data = self.user_data
        file_path = os.path.split(os.path.realpath(__file__))[0] + f'/{self.start_date[:-9]}~{self.end_date[:-9]}.csv'
        if os.path.exists(file_path):
            os.remove(file_path)
        print(file_path)
        column_names = ['姓名', '新增用例数', '更新用例数', '增改用例数', '用例维护分', '执行用例数', '用例执行分', '提交缺陷数', '流转缺陷数','非流转缺陷分', '流转缺陷分', '月提交缺陷分','基础产出分']
        try:
            with open(file_path, 'x', encoding="utf-8-sig", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=column_names)
                writer.writeheader()
                for datum in data:
                    writer.writerow(datum)
        except IOError:
            print("IO错误")
        finally:
            csv_file.close()


if __name__ == "__main__":
    p = PerformanceStatistics('2023-4-1', '2023-4-24')
    data = p.get_user_data_by_date_from_xmind_platform()
    p.create_csv_for_xmind_platform(data)


