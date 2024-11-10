pragma solidity >= 0.7.0<0.8.0;
contract MarksManagmtSys
{
  struct Student
  {
  int ID;
  string fName;
  string lName;
  int marks;
  } 
  address owner;
  int public stdCount = 0;
  mapping(int => Student)
  public stdRecords;
  modifier onlyOwner 
  {
    require(owner == msg.sender);
  } 
  {
    owner=msg.sender;
  } 
  function addNewRecords(int _ID, string memory _fName, string memory _lName, int _marks)
  public onlyOwner
  {
    stdCount = stdCount + 1;
    stdRecords[stdCount] = Student(_ID, _fName, _lName, _marks);
  } 
  function bonusMarks(int _bonus) public onlyOwner 
  {
    stdRecords[stdCount].marks = stdRecords[stdCount].marks + _bonus; }
}
