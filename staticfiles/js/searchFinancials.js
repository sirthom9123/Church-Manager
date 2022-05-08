const searchField = document.querySelector('#searchField')

const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')
const paginationContainer = document.querySelector('.pagination-container')
tableOutput.style.display = 'none'
const noResults = document.querySelector('.no-results')
const tbody = document.querySelector('.table-body')

searchField.addEventListener('keyup', (e) => {
  const searchValue = e.target.value

  if (searchValue.trim().length > 0) {
    paginationContainer.style.display = 'none'
    tbody.innerHTML = ''
    fetch('/search-financials', {
      body: JSON.stringify({ searchText: searchValue }),
      method: 'POST',
    })
      .then((res) => res.json)
      .then((data) => {
        console.log(data)
        appTable.style.display = 'none'
        tableOutput.style.display = 'block'

        console.log('data.length', data.length)

        if (data.length === 0) {
          noResults.style.display = 'block'
          tableOutput.style.display = 'none'
        } else {
          noResults.style.display = 'none'
          data.forEach((item) => {
            tbody.innerHTML += `
                    <tr>
                        <td class="contact-list-name">
                        <span
                        class="contact-list-phone d-block ">
                            ${item.entity.name}
                        </span>
                        </td>
                        <td class="contact-list-name">
                        <span
                        class="contact-list-phone d-block ">
                            ${item.project}
                        </span>
                        </td>
                        <td class="contact-list-name">
                        <span
                        class="contact-list-phone d-block ">
                            ${item.profile}
                        </span>
                        </td>
                        <td class="contact-list-name">
                        <span
                        class="contact-list-phone d-block ">
                            ${item.contact.id}
                        </span>
                        </td>
                        <td class="contact-list-name">
                        <span
                        class="contact-list-phone d-block ">
                            ${item.upload_date}
                        </span>
                        </td>
                    </tr>
                    `
          })
        }
      })
  } else {
    tableOutput.style.display = 'none'
    appTable.style.display = 'block'
    paginationContainer.style.display = 'block'
    noResults.style.display = 'none'
  }
})
