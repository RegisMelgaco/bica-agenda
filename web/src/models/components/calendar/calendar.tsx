import React, { useState } from 'react';
import './calendar.css';
import { Box, Typography } from '@mui/material';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { Dayjs } from 'dayjs';
import { StaticDatePicker } from '@mui/x-date-pickers/StaticDatePicker';
import { ptBR } from '@mui/x-date-pickers/locales';
import Schedule from '../schedule/schedule'

//theme para traduzir os componentes

//formatar a data e enviar o log pro server
const Calendar: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Dayjs | null>(null);

  const handleButtonClick = () => {
    if (selectedDate) {
      const formattedDate = selectedDate.format('DD-MM-YYYY');
      const dateJSON = { date: formattedDate };
      console.log('Data armazenada em JSON:', dateJSON);
      // Adicione aqui a lógica para enviar o JSON para um servidor ou outra ação
    } else {
      console.log('Nenhuma data selecionada');

    }
  };

  //mudar component no "ONclick"

  const [inicialCalendar, setCalendar] = useState(<Calendar />);
  const [inicialschedule, setschedule] = useState(<Schedule />);
  const swapContent = () => {
    const temp = inicialCalendar;
    setCalendar(inicialschedule);
    setschedule(temp);
  };

  return (
    <div className="calendar">
      <Box className="box">
        <Typography variant='h4'>Escolha o dia da marcação</Typography>
        <LocalizationProvider
          localeText={ptBR.components.MuiLocalizationProvider.defaultProps.localeText}
          dateAdapter={AdapterDayjs} >

          <StaticDatePicker
            disablePast

            displayStaticWrapperAs="desktop"
            timezone="system"
            slotProps={{
              toolbar: {
                //toolbarFormat: 'dd MM YYYY',
                hidden: true
              },
            }}

            value={selectedDate}
            onChange={(newValue) => setSelectedDate(newValue)}
          />
        </LocalizationProvider>

      </Box>
      <button onClick={() => {
        handleButtonClick();
        { swapContent() }
      }
      }>
        Confirmar
      </button>
    </div>




  );
}

export default Calendar;
