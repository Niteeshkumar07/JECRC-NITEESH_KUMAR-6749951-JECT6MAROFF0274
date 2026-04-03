*** Settings ***
Library     SeleniumLibrary
Resource    ../../locators/login_page_locators.robot

*** Keywords ***
Login to the application
    [Arguments]     ${login_email}    ${login_password}
    
    Click Element    ${login_link}
    Log    Clicking on login link
    
    Input Text    ${login_email_field}    ${login_email}
    Log     Entering the email
    Input Text    ${login_password_field}    ${login_password}
    Log     Entering the password
    
    Click Element    ${login_btn}
    Log   Clicking on login btn
    