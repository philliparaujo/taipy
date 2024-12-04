# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from taipy.gui import Gui

value = 50

page = """
<|{value}|metric|>

## Works (numbers)
<|{value}|metric|width=150|height=150|>
<|{value}|metric|width=300|height=300|>

## Height/width not working (px)
<|{value}|metric|width=150px|height=150px|>
<|{value}|metric|width=300px|height=300px|>

## Height/width not working (rem)
<|{value}|metric|width=150rem|height=150rem|>
<|{value}|metric|width=300rem|height=150rem|>


## Buttons (numbers)
<|Foo|button|width=150|>
<|Foo|button|width=300|>

## Buttons (px)
<|Foo-px|button|width=150px|>
<|Foo-px|button|width=300px|>

## Buttons (rem)
<|Foo-rem|button|width=150rem|>
<|Foo-rem|button|width=300rem|>
"""

Gui(page).run()
