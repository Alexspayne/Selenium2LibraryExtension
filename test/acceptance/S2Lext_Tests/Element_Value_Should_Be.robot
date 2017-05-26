*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Expected Value
    element value should be    id=input_01    Hello World

Unexpected Value
    ${ErrorMsg}=    Run Keyword And Expect Error    *    element value should be    id=input_01    Hello Worldzzz
    Should Contain    ${ErrorMsg}    Element 'id=input_01' value was not 'Hello Worldzzz', it was 'Hello World'
