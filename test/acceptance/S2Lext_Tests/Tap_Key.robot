*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Press F1
    Tap Key    ${VK_F1}
    Wait Until Page Contains Element    div_02
