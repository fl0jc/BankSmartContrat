//SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0;

contract Bank{
    mapping (address => uint) private ac_bal;
    mapping (address => uint[]) private blocks;

    function deposit_funds() public payable{
        ac_bal[msg.sender] += msg.value;
        blocks[msg.sender].push(block.number);
     }

     function withdraw_funds(uint _funds) public{
        require(ac_bal[msg.sender]>= _funds, "Insufficient Balance");
        ac_bal[msg.sender] -= _funds;
     
        (bool success,) = msg.sender.call{value: _funds}("Amount Withdrawn");
        require(success, "Insufficient Balance");
     
        blocks[msg.sender].push(block.number);
    }

    function transfer_funds(address payable receiving_address, uint _funds) public{
        require(ac_bal[msg.sender]>= _funds, "Insufficient balance");

        ac_bal[msg.sender] -= _funds;
        ac_bal[receiving_address] += _funds;

        blocks[msg.sender].push(block.number);
        blocks[receiving_address].push(block.number);
    }

    function get_balance() public view returns(uint){
        return ac_bal[msg.sender];
    }

    function get_blocks() public view returns(uint[] memory) {
        return blocks[msg.sender];
    }
}