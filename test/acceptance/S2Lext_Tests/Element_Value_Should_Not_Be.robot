*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Value Is Not
    Element Value Should Not Be    id=input_01    Potato
    Element Value Should Not Be    id=input_02    Banana
    Element Value Should Not Be    id=input_03    PineApple

Value Is
    ${ErrorMsg}=    Run Keyword And Expect Error    *    element value should not be    id=input_01    Hello World
    Should Contain    ${ErrorMsg}    Value was 'Hello World' for element 'id=input_01' while it shouldn't have
