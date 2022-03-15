import React from 'react'

import Table from "reactstrap";

const Tables = ({data, column}) => {
    return(
        <Table className="tablesorter" responsive>
            <thead className="text-primary">
                    <tr>
                      {columns.map((item, index) => <TableHeadItem item={item}/>)}
                    </tr>
            </thead>
            <tbody>
                {data.map((item, index) => <TableRow item={item} column={column}/>)}
            </tbody>

        </Table>

    )
}

const TableHeadItem = ({ item }) => <th>{item.Heading}</th>
const TableRow = ({ item, column }) => (
    <tr>
        {column.map((ColumnItem, index) => {
            return <td>{item[`${columnItem.value}`]}</td>
        })}
    </tr>
)


export default Table