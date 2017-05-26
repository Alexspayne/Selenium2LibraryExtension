*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Value Contains
    Wait Until Element Attribute Contains    input_01    Hello

Value Does Not Contain
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Element Attribute Contains    id=input_01    Potato    value  2s
    Should Contain    ${ErrorMsg}    Value 'Potato' of 'value' attribute did not appear in 2 seconds to element 'id=input_01'. It's 'value' attribute was 'Hello World'
