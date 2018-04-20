Feature: Editing customers

  Scenario: the edit button
    Given a web browser displays the "Customer List" panel
    And it displays customer "David Gahan" with the mail "depeche@gmail.com"
    When the user clicks the Edit button
    Then the browser displays the "Edit Customer" panel

  Scenario: editing general information
    Given a web browser displays the "Edit Customer" panel
    When the user changes customer's email to "depeche@mode.com"
    Then customer "David Gahan" has new email "depeche@mode.com"

  Scenario: adding comment in customer's history
    Given a web browser displays the "Edit Customer" panel
    And the "history" section is selected
    When the user wites a new comment "new comment"
    Then the comment appears in customer's history

  Scenario: adding a new transaction
    Given a web browser displays the "Edit Customer" panel
    And the "transactions" section is selected
    When the user writes "description" of the transaction as "new transaction"
    And the user writes "amount" of the transaction as "2000"
    Then the transaction appears in customer's transactions

  Scenario: adding Reward Point
    Given a web browser displays the "Edit Customer" panel
    And the "reward points" section is selected
    When the user writes "description" of the Reward Point as "new point"
    And the user writes "points" of the Reward Point as "42"
    Then the Reward Point appears in customer's Reward Points
    And the Balance is the sum of all points
