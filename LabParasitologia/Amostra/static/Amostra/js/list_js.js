$(document).ready(function () {
$('#dtBasicExample').DataTable( {
    "pageLength": 50,
    "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "Todos"] ],
  "columnDefs": [
    { "orderable": false, "targets": [4,5] }
  ],
    "language": {
  "decimal":        "",
    "emptyTable":     "Não há dados adicionados",
    "info":           "Mostrando de _START_ a _END_ : Total =  _TOTAL_ entradas",
    "infoEmpty":      "Mostrando 0 de 0 de 0 entradas",
    "infoFiltered":   "(filtrado de _MAX_ entradas)",
    "infoPostFix":    "",
    "thousands":      ",",
    "lengthMenu":     "Exibir _MENU_ entradas",
    "loadingRecords": "Carregando...",
    "processing":     "Processando...",
    "search":         "Buscar:",
    "zeroRecords":    "Não foi encontrada nenhuma entrada",
    "paginate": {
        "first":      "Primeiro",
        "last":       "Último",
        "next":       "Próximo",
        "previous":   "Anterior"
    },
    "aria": {
        "sortAscending":  ": ativada a ordenação crescente",
        "sortDescending": ": ativada a ordenação decrescente"
    }
    }
} );
$('.dataTables_length').addClass('bs-select');
});