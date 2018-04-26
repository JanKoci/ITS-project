Feature: Searching customers using filters

  Scenario: searching using customer's name
    Given a web browser displays the "Customer List" panel
    And the Customer List contains 2 customers with "Customer Name" "John"
    When the user filters the search using "Customer Name" "John"
    Then exactly 2 customers are displayed in the Customer List
    And all displayed customers have "Customer Name" "John"

  Scenario: searching using customer's email
   Given a web browser displays the "Customer List" panel
   And the Customer List contains 1 customer with "E-Mail" "regerte@gmail.com"
   When the user filters the search using "E-mail" "regerte@gmail.com"
   Then exactly 1 customers are displayed in the Customer List
   And all displayed customers have "E-Mail" "regerte@gmail.com"

  Scenario: searching using status
    Given a web browser displays the "Customer List" panel
    And the Customer List contains 0 customers with "Status" "Disabled"
    When the user filters the search using "Status" "Disabled"
    Then exactly 0 customers are displayed in the Customer List
    And all displayed customers have "Status" "Disabled"

  Scenario: searching using groups
    Given a web browser displays the "Customer List" panel
    And the Customer List contains 4 customers with "Customer Group" "Default"
    When the user filters the search using "Customer Group" "Default"
    Then exactly 4 customers are displayed in the Customer List
    And all displayed customers have "Customer Group" "Default"

  Scenario: searching using Date Added
    Given a web browser displays the "Customer List" panel
    When the user filters the search using "Date Added" "2018-04-01"
    Then all displayed customers have "Date Added" "01/04/2018"

  Scenario: searching using IP address
   Given a web browser displays the "Customer List" panel
   When the user filters the search using "IP" "88.102.254.86"
   Then all displayed customers have "IP" "88.102.254.86"
