from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类

import logging
import traceback

# 注册插件
@register(name="Fixedanswers", description="Hello Fixedanswers", version="0.2", author="max")
class FixedanswersPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    @handler(PersonNormalMessageReceived)
    @handler(GroupNormalMessageReceived)
    async def _(self, event: EventContext):
        try:
            text = event.event.text_message
            
            # 检测包含“最帅的人”的句子
            if "最帅的人" in text:
                event.prevent_default()
                event.prevent_postorder()
                event.add_return("reply", ["最帅的人是max"])
                logging.info("检测到最帅的人！")

            # 检测包含“彭于晏的女朋友”的句子
            elif "彭于晏的女朋友" in text:
                event.prevent_default()
                event.prevent_postorder()
                event.add_return("reply", ["彭于晏的老婆是"])
                logging.info("检测到彭于晏的女朋友！")

        except Exception as e:
            logging.error(traceback.format_exc())

    # 插件卸载时触发
    def __del__(self):
        pass
