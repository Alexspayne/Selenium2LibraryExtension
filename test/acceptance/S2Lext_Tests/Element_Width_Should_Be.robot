*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Expected Width
    Element Width Should Be    id=div_01    254

Unexpected Width
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Element Width Should Be    id=div_01    666
    Should Contain    ${ErrorMsg}    The width of element 'id=div_01' should have been '666' but in fact it was '254'
