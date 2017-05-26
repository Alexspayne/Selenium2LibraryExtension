*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Right Result
    Element Css Attribute Should Be    id=div_01    border-color    rgb(0, 0, 0)

Wrong Result
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Element Css Attribute Should Be    id=div_01    border-color    rgb(255, 255, 255)
    Should Contain    ${ErrorMsg}    Element locator 'id=div_01' css property 'border-color' had a value of 'rgb(0, 0, 0)' while it should have been 'rgb(255, 255, 255)'
