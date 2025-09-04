// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MockPriceOracle {
    uint256 private price;

    constructor(uint256 _initialPrice) {
        price = _initialPrice;
    }

    function setPrice(uint256 _p) external {
        price = _p;
    }

    function getPrice() external view returns (uint256) {
        return price;
    }
}
