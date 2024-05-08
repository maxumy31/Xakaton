import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';
import { TableContainer } from '@mui/material';
import Paper from '@mui/material/Paper';

class Row {
    constructor(id_, perf_, infrstr_, curm_, sci_ = null, intnat_ = null){
        this.id = id_;
        this.perf = perf_;
        this.infrstr = infrstr_;
        this.curm = curm_;
        this.sci = sci_;
        this.intnat = intnat_;
    }

    get items(){
        return this.id, this.perf, this.infrstr, this.curm, this.sci, this.intnat;
    }

    get rating(){
      return this.perf + this.infrstr + this.curm + this.sci + this.intnat;
    }
};

const rows = [
  new Row("R.E.Alexeev NNSTU", 7, 7, 7),
  new Row("Lobach", 0, 0, 0, 0, 0)
];

function preventDefault(event) {
  event.preventDefault();
}

export default function UnivRating() {
  return (
    <TableContainer component={Paper}>
      <Toolbar>
            <Typography
              component="h1"
              variant="h6"
              color="primary"
              noWrap
              sx={{ flexGrow: 1 }}
            >
              N
            </Typography>
          </Toolbar>
      <Table size="small" className="UnivRatingTable">
        <TableHead>
          <TableRow>
            <TableCell>Название</TableCell>
            <TableCell>Успеваемость</TableCell>
            <TableCell>Инфраструктура</TableCell>
            <TableCell>Учебная программа</TableCell>
            <TableCell>Наука</TableCell>
            <TableCell>Междунар. связи</TableCell>
            <TableCell>Сумма</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.perf}</TableCell>
              <TableCell>{row.infrstr}</TableCell>
              <TableCell>{row.curm}</TableCell>
              <TableCell>{row.sci}</TableCell>
              <TableCell>{row.intnat}</TableCell>
              <TableCell>{row.rating}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}