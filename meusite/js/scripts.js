document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('data.json');
    const data = await response.json();

    // Renderizar cabeçalho
    const header = document.getElementById('header');
    header.innerHTML = `
        <div class="container">
            <h1>${data.header.title}</h1>
            <ul class="menu">
                ${data.header.menu.map(
                    (item) => `
                        <li>
                            <a href="${item.link}" ${item.target ? `target="${item.target}"` : ''}>
                                ${item.text}
                            </a>
                        </li>
                    `
                ).join('')}
            </ul>
        </div>
    `;

    // Renderizar seções
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <section id="sobre" class="section">
            <div class="container">
                <h2>${data.sections.sobre.title}</h2>
                <div class="foto-container">
                    <img src="${data.sections.sobre.image}" alt="${data.header.title}" class="foto">
                </div>
                <p>${data.sections.sobre.description}</p>
            </div>
        </section>
        <section id="habilidades" class="section">
            <div class="container">
                <h2>${data.sections.habilidades.title}</h2>
                <ul>${data.sections.habilidades.items.map(item => `<li>${item}</li>`).join('')}</ul>
            </div>
        </section>
        <section id="formacao" class="section">
            <div class="container">
                <h2>${data.sections.formacao.title}</h2>
                <ul>${data.sections.formacao.items.map(item => `<li>${item}</li>`).join('')}</ul>
            </div>
        </section>
        <section id="experiencia" class="section">
            <div class="container">
                <h2>${data.sections.experiencia.title}</h2>
                <ul>${data.sections.experiencia.items.map(item => `<li>${item}</li>`).join('')}</ul>
            </div>
        </section>
        <section id="contato" class="section">
            <div class="container">
                <h2>${data.sections.contato.title}</h2>
                <p>${data.sections.contato.description}</p>
                <p>Email: <a href="mailto:${data.sections.contato.email}">${data.sections.contato.email}</a></p>
            </div>
        </section>
    `;

    // Renderizar rodapé
    const footer = document.getElementById('footer');
    footer.innerHTML = `
        <div class="container">
            <p>${data.footer.text}</p>
            <p><a href="${data.footer.githubLink}" target="_blank">${data.footer.githubText}</a></p>
        </div>
    `;
});
