pragma solidity ^0.8.26;
contract Demo {
  uint private newbal = 3500;
  function deposit(uint x) public {
    newbal += x;
}
function withdraw(uint x) public {
  if (newbal < x) {
    revert("Insufficient balance");
  }
  newbal -= x;
}
function show() public view returns (uint) {
  return newbal;
  }
}