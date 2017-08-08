-- ./app/platform/room/new_view/active_config.lua

local m_clientmain = require 'app.platform.room.clientmain'
local active_config = {
    {
        name = '�콫�踣',
        normal_state = 'welfare_01.png',
        anim_file = 'hall_res/anim_welfare.csb',
        onclick = function(v)
        end,
    },
    {
        name = '�������',
        normal_state = 'best_lucky_01.png',
        anim_file = 'hall_res/anim_best_lucky.csb',
    },
    {
        name = '������',
        normal_state = 'anim_invite_01.png',
        anim_file = 'hall_res/anim_invite_friends.csb',
        onclick = function(scene_instance)
            scene_instance.current_active_index = 1
            m_clientmain:get_instance():get_welfare_mgr():request_gift_info()
        end,
    },
    {
        name = '��������',
        normal_state = 'anim_share_01.png',
        anim_file = 'hall_res/anim_share_task.csb',
    },
    {
        name = 'ÿ�ջ',
        normal_state = 'anim_day_active_01.png',
        anim_file = 'hall_res/anim_daily_task.csb',
        onclick = function(scene_instance)
            scene_instance.current_active_index = 2
            m_clientmain:get_instance():get_welfare_mgr():request_task_list()
        end,
    },
    {
        name = 'ʤ������',
        normal_state = 'victory_task_01.png',
        anim_file = 'hall_res/anim_victory_task.csb',
        onclick = function(scene_instance)
            scene_instance.current_active_index = 3
            m_clientmain:get_instance():get_welfare_mgr():request_task_list()
        end,
    },
}

return active_config
