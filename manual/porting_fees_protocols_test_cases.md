# Porting fees protocols functional test cases

* Below Threshold Test Case (CCTP):
  - Input: Porting amount is below the threshold.
  - Actions: Initiate porting process.
  - Expected Outcome: CCTP protocol should be used, and the fees should be calculated according to the CCTP fee structure.


* Above Threshold Test Case (ChainPortX):

  - Input: Porting amount is above the threshold.
  - Actions: Initiate porting process.
  - Expected Outcome: ChainPortX protocol should be used, and the fees should be calculated according to the ChainPortX fee structure.


* Threshold Boundary Test Case (ChainPortX):

  - Input: Porting amount equals the threshold.
  - Actions: Initiate porting process.
  - Expected Outcome: ChainPortX protocol should be used, and the fees should be calculated according to the ChainPortX fee structure.


* Ethereum Bridge Test Case (ChainPortX & CCTP):

  - Input: Porting from Ethereum.
  - Actions: Initiate porting process.
  - Expected Outcome: ChainPortX should be used if the porting amount is within the threshold, otherwise CCTP should be used. Fees should be calculated based on the respective fee structures for ChainPortX and CCTP, including any extra gas fees for bridging to Ethereum.


* Non-Ethereum Bridge Test Case (ChainPortX & CCTP):

  - Input: Porting from a chain other than Ethereum.
  - Actions: Initiate porting process.
  - Expected Outcome: ChainPortX should be used if the porting amount is within the threshold, otherwise CCTP should be used. Fees should be calculated based on the respective fee structures for ChainPortX and CCTP, excluding any extra gas fees for bridging to Ethereum.


* Pay with PORTX Tokens Test Case (ChainPortX):

  - Input: Opt to pay for porting fees using PORTX tokens.
  - Actions: Initiate porting process and select PORTX tokens as the payment method.
  - Expected Outcome: PORTX tokens should be deducted automatically for the porting fees.


* Gas Cost Test Case (ChainPortX - Ethereum):

  - Input: Porting from Ethereum.
  - Actions: Initiate porting process.
  - Expected Outcome: Additional gas fees should be calculated and charged for bridging to Ethereum, according to the current gas prices.


* Gas Cost Test Case (ChainPortX - Non-Ethereum):

  - Input: Porting from a chain other than Ethereum.
  - Actions: Initiate porting process.
  - Expected Outcome: No additional gas fees should be charged for bridging to non-Ethereum chains.


---
---

#### Full disclosure

This task took about 2 minutes with the use of ChatGPT + 15 more minutes to go over the generated test cases to verify correctness and completeness.

---
---