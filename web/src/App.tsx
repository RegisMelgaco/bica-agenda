import React, { useState } from 'react';

import './App.css';
import Header from './models/components/header/header'
import Calendar from './models/components/calendar/calendar';
import SideBar from './models/components/sideBar/sideBar';
import Schedule from './models/components/schedule/schedule';



function App() {
  


  return (

    <div className='container'>
      <Header />

      <div className='App-body' >
        <div className="side" id="body"><SideBar /></div>
        <div className="content" id='body'>

          
            <Calendar />   <Schedule /> </div>
      
      
      </div>
    </div>
  );
}
export default App;
