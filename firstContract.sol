// SPDX-License-Identifier: MIT
pragma solidity >= 0.4.0 <= 0.8.15;
contract firstContract{
    uint size;
    uint[] webBytes;

    function set_webBytes(uint[] calldata x) public{
        
        webBytes = x;
    }
    function get_webBytes() public view returns (uint256[] memory){
            return webBytes;
    }
    

}