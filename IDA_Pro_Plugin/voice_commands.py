######################################################################################
#
# IDA Pro Plugin for VoiceAttack commands
#
#
# Author: James T. Bennett
#
# https://github.com/fireeye/IDA_Pro_VoiceAttack_profile
#
######################################################################################
# Copyright 2019 FireEye
#
# FireEye licenses this file to you under the Apache License, Version
# 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.
#
######################################################################################


from __future__ import print_function
import ida_kernwin
import idaapi
import idautils
import idc


class voiceattack_plugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = "Provides additional navigation functionality to FLARE's VoiceAttack profile."

    help = "https://github.com/fireeye/IDA_Pro_VoiceAttack_profile"
    wanted_name = "VoiceAttack Commands"
    wanted_hotkey = ""

    def goto_func_start(self):
        s = idc.get_func_attr(idc.here(), idc.FUNCATTR_START)
        idc.jumpto(s)

    def goto_func_end(self):
        e = idc.get_func_attr(idc.here(), idc.FUNCATTR_END)
        idc.jumpto(idc.PrevHead(e))

    def _iterate_instrs(self, advance, found):
        va = advance(idc.here())
        while (va != idc.BADADDR) and (not found(va)):
            va = advance(va)
        if va != idc.BADADDR:
            idc.jumpto(va)

    def goto_next_call(self):
        self._iterate_instrs(idc.NextHead, lambda va: idc.print_insn_mnem(va) == "call")

    def goto_prev_call(self):
        self._iterate_instrs(idc.PrevHead, lambda va: idc.print_insn_mnem(va) == "call")

    def goto_next_token(self):
        token = idaapi.get_highlighted_identifier()
        if token == "":
            return
        self._iterate_instrs(idc.NextHead, lambda va: token in idc.generate_disasm_line(va, 0))

    def goto_prev_token(self):
        token = idaapi.get_highlighted_identifier()
        if token == "":
            return
        self._iterate_instrs(idc.PrevHead, lambda va: token in idc.generate_disasm_line(va, 0))

    def jump_forward(self):
        offs = idaapi.ask_addr(0, "How many bytes to jump forward?")
        idc.jumpto(idc.here() + offs)

    def jump_back(self):
        offs = idaapi.ask_addr(0, "How many bytes to jump back?")
        idc.jumpto(idc.here() - offs)

    def init(self):
        self.hotkeys = (
            ("Ctrl-Shift-Alt-1", self.goto_func_start),
            ("Ctrl-Shift-Alt-2", self.goto_func_end),
            ("Ctrl-Shift-Alt-4", self.goto_next_token),
            ("Ctrl-Shift-Alt-5", self.goto_prev_token),
            ("Ctrl-Shift-Alt-6", self.goto_next_call),
            ("Ctrl-Shift-Alt-7", self.goto_prev_call),
            ("Ctrl-Shift-Alt-9", self.jump_forward),
            ("Ctrl-Shift-Alt-0", self.jump_back),
        )
        print("VoiceAttack plugin initialized..")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        for keystroke, method in self.hotkeys:
            ida_kernwin.del_hotkey(keystroke)
            ida_kernwin.add_hotkey(keystroke, method)

    def term(self):
        for keystroke, method in self.hotkeys:
            ida_kernwin.del_hotkey(keystroke)


def PLUGIN_ENTRY():
    return voiceattack_plugin_t()
