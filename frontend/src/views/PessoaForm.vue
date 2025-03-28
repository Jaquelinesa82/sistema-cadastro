<template>
  <div class="max-w-lg mx-auto p-6 bg-white shadow-md rounded-lg">
    <h2 class="text-2xl font-semibold mb-4 text-center">{{ pessoa.id ? 'Editar' : 'Cadastro' }} de Pessoa</h2>
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="nome" class="block font-medium">Nome</label>
        <input type="text" v-model="pessoa.nome" id="nome" required class="w-full p-2 border rounded" />
      </div>

      <div>
        <label for="data_nasc" class="block font-medium">Data de Nascimento</label>
        <input type="date" v-model="pessoa.data_nasc" id="data_nasc" required class="w-full p-2 border rounded" />
      </div>

      <div>
        <label for="cpf" class="block font-medium">CPF</label>
        <input type="text" v-model="pessoa.cpf" id="cpf" required class="w-full p-2 border rounded" />
      </div>

      <div>
        <label for="sexo" class="block font-medium">Sexo</label>
        <select v-model="pessoa.sexo" id="sexo" required class="w-full p-2 border rounded">
          <option value="m">Masculino</option>
          <option value="f">Feminino</option>
        </select>
      </div>

      <div>
        <label for="altura" class="block font-medium">Altura (em metros)</label>
        <input type="number" step="0.01" v-model="pessoa.altura" id="altura" required class="w-full p-2 border rounded" />
      </div>

      <div>
        <label for="peso" class="block font-medium">Peso (em kg)</label>
        <input type="number" v-model="pessoa.peso" id="peso" required class="w-full p-2 border rounded" />
      </div>

      <div v-if="!pessoa.id && !editando">
        <div class="text-center">
          <button type="button" @click="mostrarPesoIdeal" class="w-full bg-yellow-500 text-white py-2 rounded hover:bg-yellow-600">
            Mostrar Peso Ideal
          </button>
        </div>
      </div>

      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">
        {{ pessoa.id ? 'Atualizar' : 'Cadastrar' }} Pessoa
      </button>
    </form>

    <!-- Exibir o peso ideal da pessoa após clicar no botão -->
    <div v-if="pesoIdeal" class="mt-4 text-center bg-gray-100 p-3 rounded">
      <h4 class="font-semibold">Peso Ideal: {{ pesoIdeal }} kg</h4>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      pessoa: { nome: '', data_nasc: '', cpf: '', sexo: 'm', altura: 0, peso: 0 },
      pesoIdeal: null,  // Variável para armazenar o peso ideal calculado
      editando: false // Flag para controle de edição
    }
  },
  props: {
    pessoaEditando: {
      type: Object,
      default: () => ({})
    }
  },
  watch: {
    pessoaEditando(newPessoa) {
      if (newPessoa && newPessoa.id) {
        // Preenche os campos do formulário com os dados da pessoa a ser editada
        this.pessoa = { ...newPessoa };
        this.editando = true;  // Ativa o modo de edição
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        if (this.pessoa.id) {
          await this.editarPessoa();
        } else {
          await this.cadastrarPessoa();
        }
      } catch (error) {
        console.error('Erro ao salvar pessoa:', error)
        alert('Erro ao salvar pessoa.')
      }
    },
    async cadastrarPessoa() {
      const response = await axios.post('http://localhost:8000/api/pessoas/', this.pessoa)
      if (response.status === 201) {
        this.$emit('cadastro-sucesso');
        this.resetForm();
      }
    },
    async editarPessoa() {
      const response = await axios.put(`http://localhost:8000/api/pessoas/${this.pessoa.id}/`, this.pessoa)
      if (response.status === 200) {
        this.$emit('editar-sucesso');
        this.resetForm();
      }
    },
    calcularPesoIdeal(pessoa) {
      let pesoIdeal = pessoa.sexo === 'm' ? (72.7 * pessoa.altura) - 58 : (62.1 * pessoa.altura) - 44.7;
      return pesoIdeal.toFixed(2);
    },
    mostrarPesoIdeal() {
      this.pesoIdeal = this.calcularPesoIdeal(this.pessoa);
    },
    resetForm() {
      this.$emit('resetar-form');
      this.pessoa = { nome: '', data_nasc: '', cpf: '', sexo: 'm', altura: 0, peso: 0 };  // Limpar o formulário após submissão
      this.editando = false;
      this.pesoIdeal = null;
    }
  }
}
</script>
