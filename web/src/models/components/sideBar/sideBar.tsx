import './sideBar.css';

function SideBar() {
  return (
  
    <div className='sideBar'>
        <a href="#"><img src="./robo-icon.png" alt="Bots" className='icons'/></a>
        <a href="#"><img src="./usuario-icon.png" alt="Profile" className='icons'/></a>
        <a href="#"><img src="./engrenagem-icon.png" alt="Configurações" className='icons'/></a>
        {/* <a href="#"><img src="./agenda-icon.png" alt="Agenda" className='icons'/></a> */}
    </div>
  
  ); 
} 

export default SideBar;
