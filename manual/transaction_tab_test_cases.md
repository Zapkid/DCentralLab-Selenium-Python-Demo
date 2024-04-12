# Test Suite: Transaction History Tab

* Arrange: Login to the ChainPort app & navigate to the Transaction History page.

## Test Case 1: Verify Initial Display

### Ensure that the Transaction History tab displays correctly upon opening the app.

* Assert: Should display all page elements including expected values for:
    1. Tokens ported.
    2. Chains.
    3. Total ports.
    4. Ports in last 30 days.
    5. Ports volume.
    6. PortX details & balance.
    7. Transaction history table with list of recent transactions.

## Test Case 2: Verify Transaction Details

### Confirm that each transaction in the history list displays relevant details.
* Arrange: Open the Transaction History tab.
* Act: Select a transaction from the list.
* Assert: The transaction details page should show information such as date, time, transaction type, amount, sender/receiver addresses, and status.

## Test Case 3: Verify Sorting Functionality

### Ensure that the transaction history can be sorted by date, transaction type, or amount.
* Arrange: Open the Transaction History tab.
* Act: Try sorting transactions by date, type, and amount.
* Assert: Transactions should rearrange themselves according to the selected sorting criteria.

## Test Case 4: Verify Pagination

### Check if pagination works correctly when there are multiple transactions.
* Arrange: Open the Transaction History tab.
* Act: Scroll through the list to reach the end.
* Assert: If there are more transactions than can fit on one page, additional pages should load automatically, or there should be a button to load more transactions.

## Test Case 5: Verify Search Functionality

### Confirm that users can search for specific transactions using keywords.
* Arrange: Open the Transaction History tab.
* Act: Locate the search bar and enter a keyword related to a transaction.
* Assert: The transaction list should filter and display only transactions matching the entered keyword.

## Test Case 6: Verify Refresh Functionality

### Ensure that users can manually refresh the transaction history.
* Arrange: Open the Transaction History tab.
* Act: Locate the refresh button and click on it.
* Assert: The transaction history should update to display the latest transactions.

## Test Case 7: Verify Interaction with Transactions

### Test interactions with individual transactions such as clicking for more details or copying transaction IDs.
* Arrange: Open the Transaction History tab.
* Act: Click on a transaction.
* Assert: The app should respond appropriately, either displaying more details of the transaction or allowing the user to copy relevant information.

## Test Case 8: Verify Empty State

### Check the behavior when there are no transactions to display.
* Arrange: Disconnect the MetaMask wallet or clear transaction history.
* Act: Open the Transaction History tab.
* Assert: A message or placeholder should inform the user that there are no transactions to display.