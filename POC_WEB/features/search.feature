@search
Feature: Pesquisar Santander
    As an user
    I want search for Santander website
    So I can enter Santanders website

    Scenario: Search for Santander website
        Given I am in Google website
        When I search for Santander
        And access the first result
        Then I enter Santanders website

