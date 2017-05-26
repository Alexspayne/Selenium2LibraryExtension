*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Expected Color
    Element Text Color Should Be    id=span_01    rgba(255, 255, 255, 1)
    Element Text Color Should Be    id=First_Paragraph    rgba(0, 0, 0, 1)

Unexpected Color
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Element Text Color Should Be    id=span_01    rgba(0, 0, 0, 1)
    Should Contain    ${ErrorMsg}    Element locator 'id=span_01' css property 'color' had a value of 'rgba(255, 255, 255, 1)' while it should have been 'rgba(0, 0, 0, 1)'
