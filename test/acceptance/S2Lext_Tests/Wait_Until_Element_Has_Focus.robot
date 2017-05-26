*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Has Focus
    Set Element Focus    id=input_01
    Wait Until Element Has Focus    id=input_01
    Set Element Focus    id=input_02
    Wait Until Element Has Focus    id=input_02
    Set Element Focus    id=input_03
    Wait Until Element Has Focus    id=input_03

Doesn't Have Focus
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Element Has Focus    id=input_01
    Should Contain    ${ErrorMsg}    Element 'id=input_01' did not get focus after 10 seconds
