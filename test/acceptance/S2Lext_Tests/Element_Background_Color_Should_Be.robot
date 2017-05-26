*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Expected Color
    Element Background Color Should Be    id=div_01    rgba(255, 0, 0, 1)

Unexpected Color
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Element Background Color Should Be    id=div_01    rgba(255, 255, 255, 1)
    Should Contain    ${ErrorMsg}    Element locator 'id=div_01' css property 'background-color' had a value of 'rgba(255, 0, 0, 1)' while it should have been 'rgba(255, 255, 255, 1)'
