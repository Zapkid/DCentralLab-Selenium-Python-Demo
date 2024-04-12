# Test Suite: Transaction History Tab

* Arrange: Login to the ChainPort app & navigate to the Transaction History page.

## Test Case: Verify Initial Display

### Ensure that the Transaction History tab displays correctly upon opening the app.

* Assert: Should display all page elements including expected values & style for:
    1. Title.
    2. Account link.
    3. Tabs (Current Balances, Transaction history & My Referrals)
    4. Tokens ported.
    5. Chains.
    6. Total ports.
    7. Ports in last 30 days.
    8. Ports volume.
    9. PortX details & balance.
    10. Transaction history table with list of recent transactions & Download CSV button.


## Test Case: Verify Interaction with Port balance dropdown

### Test interactions with the Port balance dropdown.

* Act: Click on the Port balance dropdown.
* Assert: The dropdown should open.


## Test Case: Verify Transaction Details

### Confirm that each transaction in the history list displays relevant details.

* Act: View/Select each transaction from the list.
* Assert: The transaction details should show expected information such as date, token type & amount, from & to which chain and port fees.


## Test Case: Verify Interaction with Transactions

### Test interactions with individual transactions such as clicking for more details or clicking on outgoing link.

* Act: Click on a transaction / outgoing link.
* Assert: The app should respond appropriately, either displaying more details of the transaction or navigating to the outgoing link url.


## Test Case: Verify newly added ported token transaction is displayed

### Confirm data updated on page refresh after adding a new ported token.

* Arrange: Add a new ported token transaction.
* Act: Refresh the page.
* Assert: The app should display updated data in the totals section, port balance & transaction history should include the newly added transaction.


## Test Case: Verify Download transactions history CSV Functionality

### Ensure that the Download transactions history CSV button downloads the expected data in a CSV file format.

* Act: Click on the Download transactions history CSV button.
* Assert: That the expected data is downloaded in a CSV file format.


## Test Case: Verify Sorting Functionality

### Ensure that the transaction history columns can be sorted.

* Act: Try sorting transactions by date, token, from, to & port fee.
* Assert: Transactions should rearrange themselves according to the selected sorting criteria.


## Test Case: Verify Pagination

### Check if pagination works correctly when there are many transactions / multiple transaction pages.

* Act: Scroll through the list to reach the end.
* Assert: That additional pages load automatically, or there should be a button to load more transactions.


## Test Case: Verify Empty State

### Check the behavior when there are no transactions to display.

* Arrange: Disconnect the MetaMask wallet or clear transaction history.
* Act: Open the Transaction History tab.
* Assert: A message or placeholder should inform the user to connect a wallet / that there are no transactions to display.


## Test Case: Verify navigation to account page 

### Check navigation to account page

* Act: Click on the account link button.
* Assert: Should navigate to the account page.


## Test Case: Verify navigation to other tabs 

### Check navigation to Current Balances & My Referrals tabs.

* Act: Click on Current Balances / My Referrals tab.
* Assert: Should display the Current Balances / My Referrals tabs UI.