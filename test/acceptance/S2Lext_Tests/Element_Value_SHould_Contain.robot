*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Excepted Value
    Element Value Should Contain    id=input_01    Hello
    Element Value Should Contain    id=input_02    Hello New
    Element Value Should Contain    id=input_03    Hello Brand

Unexpected Value
    ${ErrorMsg}=    Run Keyword And Expect Error    *    element value should contain    id=input_01    Hellllllo
    Should Contain    ${ErrorMsg}    Value 'Hellllllo' did not appear in element 'id=input_01'. It's value was 'Hello World'
