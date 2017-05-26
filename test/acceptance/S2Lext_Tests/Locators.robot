*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
input
    Set Element Focus    id=input_01
    ${value}=    Get Value    input=current
    Should Contain    ${value}    Hello World

meta_name
    Wait Until Page Contains Element    meta_name=language    3s

first_tag
    ${value}=    Get Text    first_tag=p
    Should Contain    ${value}    Hello! I'm the first paragraph

last_tag
    ${value}=    Get Text    last_tag=p
    Should Contain    ${value}    Hello! I'm the last paragraph
