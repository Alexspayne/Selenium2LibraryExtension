*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Element Attribute Is
    Wait Until Element Attribute Is    input_01    Hello World
    Wait Until Element Attribute Is    input_02    Hello New World

Element Attribute Is Not
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Element Attribute Is    id=input_01    Potato    value  2s
    Should Contain    ${ErrorMsg}    Element 'id=input_01' attribute 'value' value was not Potato after 10 seconds
