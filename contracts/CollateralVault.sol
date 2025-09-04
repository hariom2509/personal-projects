// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./uUSD.sol";
import "./MockPriceOracle.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CollateralVault is Ownable {
    uUSD public stablecoin;
    MockPriceOracle public oracle;
    mapping(address => uint256) public collateral;

    uint256 public constant COLLATERAL_RATIO = 150; // 150%
    uint256 public constant DECIMALS = 1e18;

    constructor(address _stablecoin, address _oracle) {
        stablecoin = uUSD(_stablecoin);
        oracle = MockPriceOracle(_oracle);
    }

    function depositAndMint() external payable {
        require(msg.value > 0, "deposit > 0");
        uint256 price = oracle.getPrice();
        uint256 usdValue = (msg.value * price) / DECIMALS;
        uint256 usdToMint = (usdValue * 100) / COLLATERAL_RATIO;

        collateral[msg.sender] += msg.value;
        stablecoin.mint(msg.sender, usdToMint);
    }

    // redeem expects user to transfer uUSD to vault first; then call redeem to get ETH back
    function redeem(uint256 usdAmount) external {
        require(usdAmount > 0, "usd > 0");
        // vault must hold tokens transferred by user
        uint256 vaultBalance = stablecoin.balanceOf(address(this));
        require(vaultBalance >= usdAmount, "vault lacks tokens");
        stablecoin.burn(address(this), usdAmount);

        uint256 price = oracle.getPrice();
        uint256 ethToReturn = (usdAmount * COLLATERAL_RATIO * DECIMALS) / (price * 100);
        require(collateral[msg.sender] >= ethToReturn, "not enough collateral");

        collateral[msg.sender] -= ethToReturn;
        payable(msg.sender).transfer(ethToReturn);
    }
}
