import './schedule.css';

function Schedule() {
  return (
    <div className='scheduleTable'>
      <table>
        <thead>
          <tr>
            <th>HORÁRIO</th>
            <th>NOME</th>
            <th>STATUS</th>
          </tr>
        </thead>
        <tbody>
        
          <tr>
          
            <td>HORÁRIO 1</td>
            <td>NOME 1</td>
            <td><button>Marcar</button>
            </td>
          </tr>
          
          
          <tr>
            <td>HORÁRIO 2</td>
            <td>NOME 2</td>
            <td>
              <button>Marcar</button>
            </td>
          </tr>
          <tr>
            <td>HORÁRIO 3</td>
            <td>NOME 3</td>
            <td>
              <button>Marcar</button>
            </td>
          </tr>
          
        </tbody>
      </table>
    </div>
  );
}

export default Schedule;
