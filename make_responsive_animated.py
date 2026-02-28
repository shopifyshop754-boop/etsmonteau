import os
import re

files_to_update = ['index.html', 'services.html', 'contact.html']

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the mobile menu CSS classes to be animated and cover the full screen smoothly
    old_menu_class_pattern = r'class="fixed top-\[\d+px\].+?z-40 hidden flex-col items-center justify-center gap-8 text-xl font-bold opacity-0 transition-opacity duration-300"'
    
    new_menu_class = 'class="fixed inset-0 pt-28 pb-10 overflow-y-auto bg-white/95 dark:bg-slate-900/95 backdrop-blur-md shadow-2xl z-40 flex flex-col items-center justify-center gap-8 text-xl font-bold opacity-0 -translate-y-full transition-all duration-500 pointer-events-none"'
    
    if re.search(old_menu_class_pattern, content):
        content = re.sub(old_menu_class_pattern, new_menu_class, content)
    else:
        # Fallback if pattern slightly differs
        content = re.sub(r'id="mobile-menu"\s+class="[^"]+"', f'id="mobile-menu" {new_menu_class}', content)

    # 2. Update the JavaScript for toggling the menu smoothly (remove 'hidden'/'flex' toggle, use opacity, translation, pointer-events)
    old_js = """btn.addEventListener('click', () => {
                if (menu.classList.contains('hidden')) {
                    menu.classList.remove('hidden');
                    menu.classList.add('flex');
                    setTimeout(() => {
                        menu.classList.remove('opacity-0');
                        menu.classList.add('opacity-100');
                    }, 10);
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-xmark');
                } else {
                    menu.classList.remove('opacity-100');
                    menu.classList.add('opacity-0');
                    setTimeout(() => {
                        menu.classList.add('hidden');
                        menu.classList.remove('flex');
                    }, 300);
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            });"""

    new_js = """btn.addEventListener('click', () => {
                const isOpen = menu.classList.contains('opacity-100');
                if (!isOpen) {
                    menu.classList.remove('opacity-0', '-translate-y-full', 'pointer-events-none');
                    menu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-xmark');
                } else {
                    menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
                    menu.classList.add('opacity-0', '-translate-y-full', 'pointer-events-none');
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            });"""
            
    # Remove existing JS and replace
    if "btn.addEventListener('click'" in content:
        # Regex to replace the whole event listener block
        content = re.sub(r"btn\.addEventListener\('click',\s*\(\)\s*=>\s*\{.*?(icon\.classList\.add\('fa-bars'\);\s*\}\s*\});", new_js, content, flags=re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files for sweet responsive mobile animations.")
