// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVote {
    function vote(uint256 _candidateId) external;
}

contract Elector {
    address public voterAddress;
    address public voteContractAddress;
    string public fullName;
    string public company;
    string public position;
    string public email;
    uint public votesMade;

    modifier onlyVoter() {
        require(msg.sender == voterAddress, "Only the voter can call this function");
        _;
    }

    constructor(address _voterAddress, address _voteContractAddress, string memory _fullName, string memory _company, string memory _position, string memory _email) {
        voterAddress = _voterAddress;
        voteContractAddress = _voteContractAddress;
        fullName = _fullName;
        company = _company;
        position = _position;
        email = _email;
        votesMade = 0;
    }

    function vote(uint256 _candidateId) external onlyVoter {
        IVote(voteContractAddress).vote(_candidateId);
        votesMade++;
    }

    function voterInfo() external view returns (string memory) {
        return string(abi.encodePacked("Full Name: ", fullName, ", Company: ", company, ", Position: ", position, ", Email: ", email, ", Votes Made: ", uint2str(votesMade), ", Voter Address: ", toHexString(voterAddress, 20)));
    }

    function uint2str(uint _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint j = _i;
        uint len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint k = len;
        while (_i != 0) {
            k = k-1;
            uint8 temp = (48 + uint8(_i - _i / 10 * 10));
            bytes1 b1 = bytes1(temp);
            bstr[k] = b1;
            _i /= 10;
        }
        return string(bstr);
    }

    function toHexString(address _addr, uint256 _len) internal pure returns (string memory) {
        bytes32 value = bytes32(uint256(uint160(_addr)));
        bytes memory alphabet = "0123456789abcdef";
        bytes memory str = new bytes(2 * _len + 2);
        str[0] = "0";
        str[1] = "x";
        for (uint256 i = 0; i < _len; i++) {
            str[2+i*2] = alphabet[uint8(value[i + 12] >> 4)];
            str[3+i*2] = alphabet[uint8(value[i + 12] & 0x0f)];
        }
        return string(str);
    }
}
