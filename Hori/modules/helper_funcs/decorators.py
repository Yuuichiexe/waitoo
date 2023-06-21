"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2023-2024, Eren-YeagerO, [ https://github.com/Eren-YeagerO]
Copyright (c) 2023-2024, Programmer Network, [ https://github.com/Eren-YeagerO/Hori ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from typing import List, Optional, Union

from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
)
from telegram.ext.filters import BaseFilter

from Hori import LOGGER
from Hori import dispatcher as d
from Hori.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)


class HoriTelegramHandler:
    def __init__(self, d):
        self._Hori_PTB = d

    def command(
        self,
        command: str,
        filters: Optional[BaseFilter] = None,
        admin_ok: bool = False,
        pass_args: bool = False,
        pass_chat_data: bool = False,
        run_async: bool = True,
        can_disable: bool = True,
        group: Optional[Union[int]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._Hori_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._Hori_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[HoriCMD] Loaded handler {command} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._Hori_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._Hori_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[HoriCMD] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        run_async: bool = True,
        group: Optional[Union[int]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._Hori_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        ),
                        group,
                    )
                else:
                    self._Hori_PTB.add_handler(
                        MessageHandler(pattern, func, run_async=run_async), group
                    )
                LOGGER.debug(
                    f"[HoriMSG] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._Hori_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        )
                    )
                else:
                    self._Hori_PTB.add_handler(
                        MessageHandler(pattern, func, run_async=run_async)
                    )
                LOGGER.debug(
                    f"[HoriMSG] Loaded filter pattern {pattern} for function {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._Hori_PTB.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, run_async=run_async
                )
            )
            LOGGER.debug(
                f"[HoriCALLBACK] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        run_async: bool = True,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._Hori_PTB.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    run_async=run_async,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[HoriINLINE] Loaded inlinequery handler with pattern {pattern} for function {func.__name__} | PASSES USER DATA: {pass_user_data} | PASSES CHAT DATA: {pass_chat_data} | CHAT TYPES: {chat_types}"
            )
            return func

        return _inlinequery


Horicmd = HoriTelegramHandler(d).command
Horimsg = HoriTelegramHandler(d).message
Horicallback = HoriTelegramHandler(d).callbackquery
Horiinline = HoriTelegramHandler(d).inlinequery
