const fs = require('fs');

// Read the JSON file
const data = JSON.parse(fs.readFileSync('Tutorias_G42.json', 'utf8'));

// Function to extract Vimeo ID from iframe content
function extractVimeoId(iframeContent) {
    const match = iframeContent.match(/player\.vimeo\.com\/video\/(\d+)/);
    return match ? match[1] : null;
}

// Function to recursively search for tabs with Vimeo links
function findVimeoSessions(obj, sessions = []) {
    if (typeof obj === 'object' && obj !== null) {
        // Check if this object has tabs
        if (Array.isArray(obj.tabs)) {
            obj.tabs.forEach(tab => {
                if (tab.tab_title && tab.tab_content) {
                    const vimeoId = extractVimeoId(tab.tab_content);
                    if (vimeoId) {
                        sessions.push({
                            title: tab.tab_title,
                            vimeo_id: vimeoId,
                            vimeo_url: `https://vimeo.com/${vimeoId}`
                        });
                    }
                }
            });
        }

        // Recursively search in all values
        Object.values(obj).forEach(value => {
            findVimeoSessions(value, sessions);
        });
    } else if (Array.isArray(obj)) {
        obj.forEach(item => {
            findVimeoSessions(item, sessions);
        });
    }

    return sessions;
}

// Extract all sessions
console.log("Extrayendo sesiones con enlaces de Vimeo...");
const sessions = findVimeoSessions(data);

console.log(`Se encontraron ${sessions.length} sesiones`);

// Save to CSV
const csvContent = 'title,vimeo_id,vimeo_url\n' +
    sessions.map(s => `"${s.title}",${s.vimeo_id},${s.vimeo_url}`).join('\n');
fs.writeFileSync('Sesiones_Vimeo_G42.csv', csvContent, 'utf8');

console.log('Archivo CSV guardado en: Sesiones_Vimeo_G42.csv');

// Also save to a text file for easy reading
let txtContent = "SESIONES DEL DIPLOMADO EN BIODESPROGRAMACIÓN - GENERACIÓN 42\n";
txtContent += "=".repeat(80) + "\n\n";
sessions.forEach((session, i) => {
    txtContent += `${i + 1}. ${session.title}\n`;
    txtContent += `   Vimeo URL: ${session.vimeo_url}\n`;
    txtContent += `   Vimeo ID: ${session.vimeo_id}\n\n`;
});

fs.writeFileSync('Sesiones_Vimeo_G42.txt', txtContent, 'utf8');

console.log('Archivo de texto guardado en: Sesiones_Vimeo_G42.txt');
console.log('\n¡Extracción completada!');
