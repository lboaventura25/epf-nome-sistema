%rebase('layout', title='Funcionários')

<section class="employees-section fundo-amarelo-degrade">
    <div class="section-header">
        <h1 class="section-title"><i class="fas fa-employees"></i> Gestão de Usuários</h1>
        <a href="/employees/add" class="btn btn-primary">
            <i class="fas fa-plus"></i> Novo Usuário
        </a>
    </div>

    <div class="table-container">
        <table class="styled-table">
            
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Cargo</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for u in employees:
                <tr>
                    <td>{{u.id}}</td>
                    <td>{{u.name}}</td>
                    <td><a href="mailto:{{u.email}}">{{u.email}}</a></td>
                    <td>{{u.formatted_postiton}}</td>
                    
                    <td class="actions">
                        <a href="/employees/edit/{{u.id}}" class="btn btn-sm btn-edit">
                            <i class="fas fa-edit"></i> Editar
                        </a>

                        <form action="/employees/delete/{{u.id}}" method="post" 
                            onsubmit="return confirm('Tem certeza?')">
                            <button type="submit" class="btn btn-sm btn-danger">
                                <i class="fas fa-trash-alt"></i> Excluir
                            </button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
        </div>
</section>