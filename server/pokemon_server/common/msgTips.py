# coding:utf-8
# Purpose: 消息提示CODE常量集合
# Created: 2012-12-7

FAIL_MSG_LOGIN_WRONG_ACCOUNT = 1
FAIL_MSG_LOGIN_PLAYERNAME_EXIST = 2
FAIL_MSG_LOGIN_PLAYERNAME_ISEMPTY = 3
FAIL_MSG_LOGIN_LINE_TIME_OUT = 4
FAIL_MSG_ALREADY_LOGIN = 6
FAIL_MSG_INVALID_PASSWORD = 7     # 删除角色时密码校验失败
FAIL_MSG_DELETE_ROLE = 8     # 删除角色失败
FAIL_MSG_LOAD_PLAYER = 9     # 加载玩家失败

FAIL_MSG_INVALID_REQUEST = 10    # 通用 无效请求
FAIL_MSG_SERVERNOTOPEN = 15  # 服务器暂未开放
FAIL_MSG_ALREADY_CREATEROLE = 16  # 已经创建角色
# 11 - 19 预留
FAIL_MSG_CLOSE_SERVER = 19  # 关闭服务器
FAIL_MSG_NOT_ACTIVATED = 20     # 未激活
FAIL_MSG_INVALID_CODE = 21     # 无效的激活码
FAIL_MSG_LOGIN_PLAYERNAME_FORBIDDEN = 22
# 禁用的用户名
FAIL_MSG_SDK_LOGIN_FAILED = 23     # SDK登录失败
FAIL_MSG_SDK_START_PAY_FAILED = 24     # 生成支付流水号失败
SUCCESS_MSG_PAY_OK = 25     # 支付成功
SUCCESS_MSG_PAY_FAIL = 26     # 支付失败

FAIL_MSG_NAME_TOOLONG_TO_CREATE = 27    # 名字过长无法使用
FAIL_MSG_NAME_TOOSHORT_TO_CREATE = 28    # 名字过短无法使用
# 29 保留

FAIL_MSG_NOT_OPENED = 31     # 功能未开启
FAIL_MSG_IGNORE = 32     # 客户端无任何提示的错误码
FAIL_MSG_POSITION_VALIDATION = 33     # 服务器位置校验失败

FAIL_MSG_WITH_REASON = 34     # 服务器无CODE带REASON的错误消息

FAIL_MSG_ILLEGAL_OPERATION = 35    # 帐号涉及非法操作

PROMPT_ONLINE_PLAYER_GIVEN_SP = 50  # 在线玩家赠送能量

FAIL_MSG_LOGIN_OLDVERSION = 51     # 版本太旧
FAIL_MSG_REGISTERLIMIT = 52     # 今日已经注册了3次

FAIL_MSG_SERVER_CLOSED = 55  # 世界服务器已经关闭

# 60 - 90 预留，主动踢出玩家前发送的消息
FAIL_MSG_KICKED = 60     # 被人踢了


FAIL_MSG_PVP_CLOSED = 1385  # pvp已经关闭
FAIL_MSG_PVP_FIGHT_HISTORY_MISSED = 1386  # 战斗回放不存在
FAIL_MSG_PVP_UPROAR_NOT_ENOUGH_POWER = 1310  # 大闹天宫战斗力不足，匹配不到对手时返回的错误码

FAIL_MSG_FACTION_ALREADY_CANCEL_APPLY = 1400  # 玩家已经取消公会加入申请了

FAIL_MSG_FACTION_NAME_EMPTY = 1401  # 公会名称为空
FAIL_MSG_FACTION_NAME_TOOLONG = 1402  # 公会名称过长
FAIL_MSG_FACTION_NAME_TOOSHORT = 1403  # 公会名称过短
FAIL_MSG_FACTION_NAME_INVALID = 1404  # 非法的公会名称

FAIL_MSG_FACTION_MEMBER_ALREADY_QUIT = 1405  # 玩家已经退出了公会
FAIL_MSG_FACTION_ALREADY_HAD_FACTION = 1406  # 玩家已经有公会了
FAIL_MSG_FACTION_ALREADY_APPLYED = 1407  # 玩家已经申请加入公会了

FAIL_MSG_FACTION_IS_NOT_IN_FACTION = 1408  # 玩家不属于这个公会
FAIL_MSG_FACTION_HAS_NOT_FACTION = 1409  # 还没有加入公会
FAIL_MSG_FACTION_DUPLICATE_FACTION_NAME = 1410  # 已存在的公会名称
FAIL_MSG_FACTION_CREATE_FAIL = 1411  # 创建公会失败
FAIL_MSG_FACTION_PERMISSION_DENIED = 1412  # 权限不足
FAIL_MSG_FACTION_NOT_THIS_FACTION = 1413  # 这个公会已经不存在了
FAIL_MSG_FACTION_MEMBERS_LIMIT_EXCEED = 1414  # 这个公会已经人满为患了
FAIL_MSG_FACTION_CAN_NOT_DISMISS = 1415  # 无法解散人数大于一的公会
FAIL_MSG_FACTION_ALREADY_LEADER = 1416  # 已经是会长了
FAIL_MSG_FACTION_LEADER_CAN_NOT_QUIT = 1417  # 会长不能退出公会
FAIL_MSG_FACTION_PLAYER_NOT_FOUND = 1418  # 找不到这个玩家

FAIL_MSG_FACTION_NOT_APPLYED = 1419  # 没有申请加入
FAIL_MSG_FACTION_ALREADY_INVITED = 1420  # 已经收到公会的邀请了
FAIL_MSG_FACTION_CAN_NOT_STRENGTHEN = 1421  # 强化未开启
FAIL_MSG_FACTION_CAN_NOT_LEAVE = 1422  # 加入公会24小时内不能退出/踢出
FAIL_MSG_FACTION_NOT_ENOUGH_LEVEL = 1423  # 玩家低于8级不能邀请
FAIL_MSG_FACTION_NOT_ENOUGH_GOLD = 1424  # 钻石不足
FAIL_MSG_FACTION_EXCEED_DAILY_DONATE_LIMIT = 1425  # 超过每日贡献限额
FAIL_MSG_FACTION_NOT_ENOUGH_MONEY = 1426  # 金币不足
FAIL_MSG_FACTION_MAX_LEVEL = 1427  # 等级达到上限
FAIL_MSG_FACTION_NOT_ENOUGH_TOTALFP = 1428  # 贡献不足
FAIL_MSG_FACTION_NOT_ENOUGH_FP = 1429  # 声望不足
FAIL_MSG_FACTION_CAN_NOT_THRONE_TO_NEWER = 1430  # 公会会长不能转让给加入公会低于3天的玩家
FAIL_MSG_FACTION_CAN_NOT_JOIN_WILL_DISMISS_FACTION = 1431  # 不能加入一个即将解散的公会

FAIL_MSG_MALL_EXCEED_BUY_SP_LIMIT = 1432  # 超过能量购买次数限制
FAIL_MSG_MALL_EXCEED_BUY_FB_LIMIT = 1433  # 超过副本购买次数限制

# 不能邀请玩家加入一个即将解散的公会
FAIL_MSG_FACTION_CAN_NOT_INVITE_TO_WILL_DISMISS_FACTION = 1434
# 不能允许玩家加入一个即将解散的公会
FAIL_MSG_FACTION_CAN_NOT_ALLOW_JOIN_WILL_DISMISS_FACTION = 1435
FAIL_MSG_FACTION_ALREADY_DISMISSED = 1436  # 公会已经被解散了
FAIL_MSG_FACTION_DONATE_AMOUNT_INVALID = 1437  # 非法捐献金额
FAIL_MSG_FACTION_DENY_APPLY = 1438  # 公会拒绝加入

FAIL_MSG_EQUIP_NOT_FOUND = 1500  # 装备不存在
FAIL_MSG_EQUIP_EXCEED_LEVEL_LIMITED = 1501  # 超过等级上限
FAIL_MSG_EQUIP_NOT_ENOUGH_MONEY = 1502  # 金币不足
FAIL_MSG_EQUIP_EXCEED_ADVANCE_LIMITED = 1503  # 超过进阶上限

FAIL_MSG_ROB_ALREADY_ROBBED = 1600  # 正在被掠夺
FAIL_MSG_ROB_ALREADY_HARVESTED = 1601  # 已经被收获了
FAIL_MSG_ROB_ALREADY_IN_PROTECTION = 1602  # 正处于保护期
FAIL_MSG_ROB_TIMEOUT = 1603  # 掠夺超时
FAIL_MSG_ROB_ALREADY_FOUGHT = 1604  # 已经掠夺过了
FAIL_MSG_ROB_INVALID_TARGET = 1605  # 无效的目标
FAIL_MSG_ROB_ALREADY_REVENGED = 1606  # 已经复仇过了
FAIL_MSG_ROB_NOT_ENOUGH_TO_REFRESH_ROB_LIST = 1607  # 消耗不足，无法刷新列表
FAIL_MSG_ROB_NOT_ENOUGH_TO_COLLECT = 1608  # 消耗不足， 无法收集
FAIL_MSG_ROB_NOT_ENOUGH_ROB_COUNT = 1609  # 掠夺次数不足

# 聊天
FAIL_MSG_FRIEND_CHAT_SPEAK_TOO_FREQUENTLY = 1699  # 发言过于频繁
FAIL_MSG_CHAT_SPEAK_TOO_FREQUENTLY = 1700  # 发言过于频繁


# 重铸
FAIL_MSG_COMPOSE_NOT_ENOUGH_STUFFS = 1701  # 材料不足

FAIL_MSG_PLAYER_NOT_FOUND = 1800  # 玩家不存在

FAIL_MSG_FRIEND_CAN_NOT_APPLY_SELF = 1801  # 不能添加自己为好友
FAIL_MSG_FRIEND_ALREADY_FIREND = 1802  # 对方已经是你的好友了
FAIL_MSG_FRIEND_ALREADY_APPLYED_YOU = 1803  # 对方已经申请添加你为好友了
FAIL_MSG_FRIEND_ALREADY_APPLYED = 1804  # 已经申请添加对方为好友了
FAIL_MSG_FRIEND_LIMITED_EXCEED = 1805  # 对方已达好友上限

FAIL_MSG_FRIENDFB_ALREADY_DISAPPEARED = 1810  # 秘境已经消失
FAIL_MSG_FRIENDFB_ALREADY_DEAD = 1811  # 秘境boss已死亡

FAIL_MSG_CANT_TAP_ONEKEY = 1900  # vip不足，不能使用一键扫荡群魔乱舞


# VIP PACKS
FAIL_MSG_VIP_PACKS_EXPIRED = 2000  # VIP礼包超出可以购买的时间了

# GROUP
FAIL_MSG_GROUP_NOT_FOUND = 2500  # 找不到同门
FAIL_MSG_GROUP_ALREADY_JOINED = 2501  # 已经加入同门了
FAIL_MSG_GROUP_LIMITED_EXCEED = 2502  # 满人
FAIL_MSG_GROUP_ALREADY_APPLIED = 2503  # 已经申请加入了
FAIL_MSG_GROUP_HAS_NOT_JOINED = 2504  # 还未加入同门
FAIL_MSG_GROUP_NOT_IN_THIS = 2506  # 不是这个同门的成员
FAIL_MSG_GROUP_ALREADY_INVITED = 2507  # 已经邀请过了
FAIL_MSG_GROUP_NAME_EMPTY = 2508  # 同门名称为空
FAIL_MSG_GROUP_NAME_TOOLONG = 2509  # 同门名称过长
FAIL_MSG_GROUP_NAME_TOOSHORT = 2510  # 同门名称过短
FAIL_MSG_GROUP_NAME_INVALID = 2511  # 同门名称非法
FAIL_MSG_GROUP_PERMISSION_DENIED = 2512  # 权限不足
FAIL_MSG_GROUP_DUPLICATE_FACTION_NAME = 2513  # 已存在的同门名称
FAIL_MSG_GROUP_CREATE_FAIL = 2514  # 创建同门失败
FAIL_MSG_GROUP_KICK_TOO_FREQUENTLY = 2515  # 最近24小时您已经清理过门户啦
FAIL_MSG_GROUP_KICKED_RECENTLY = 2516  # 24小时内曾被驱逐，不能加入新同门
FAIL_MSG_GROUP_DISMISSED = 2517  # 同门已经解散
FAIL_MSG_GROUP_KICK_TOO_FREQUENTLY_TO_INVITED = 2518  # 24小时内清理过门户，无法邀请新的玩家
FAIL_MSG_GROUP_KICK_TOO_FREQUENTLY_TO_ALLOW = 2519  # 24小时内踢除过同门成员，暂时无法通过申请

FAIL_MSG_GROUP_GVE_START_SOLO = 2600  # 单枪匹马不是好作风！
FAIL_MSG_GROUP_GVE_NOT_OPEN = 2601  # 活动未开启
FAIL_MSG_GROUP_GVE_ALREADY_STARTED = 2602  # 活动已经开始了
FAIL_MSG_GROUP_GVE_ALREADY_END = 2603  # 活动已经结束了

FAIL_MSG_FIGHT_VERIFY_FAILED = 3000  # 战斗校验失败
FAIL_MSG_DAILY_CAMPAIGN_CLOSED = 3001  # 每日PVP活动已结束
FAIL_MSG_DAILY_NOT_TARGET = 3002  # 每日PVP
FAIL_MSG_DAILY_RED_NOT_ENOUGH = 3003   # 红包被领完
FAIL_MSG_DAILY_RED_TIMEOUT = 3004  # 红包超时
FAIL_MSG_MAT_NOT_ENOUGH = 4002  # 所需材料不足
FAIL_MSG_MAT_EXCHANGE_LIMIT = 4003  # 兑换次数达到上限

FAIL_MSG_CITY_CAMPAIGN_CLOSED = 5001  # 黄金城活动结束结束

FAIL_MSG_STAR_PACKS_UNAVAILABLE = 5002  # 星级奖励，星星不够
FAIL_MSG_STAR_PACKS_TAKEN = 5003  # 星级奖励，领过了
FAIL_MSG_STAR_PACKS_NOT_EXISTS = 5004  # 星级奖励，不存在

FAIL_MSG_CLIMB_TOWER_ACCREDIT_LIMITED_EXCEED = 5100  # 满人
FAIL_MSG_CLIMB_TOWER_ACCREDIT_LOW_FLOOR = 5101  # 低于当前派驻层
FAIL_MSG_CLIMB_TOWER_TARGET_UNAVAILABLE = 5102  # 对手不在当前派驻层
FAIL_MSG_CLIMB_TOWER_CHEST_TAKEN = 5103  # 领取过了
