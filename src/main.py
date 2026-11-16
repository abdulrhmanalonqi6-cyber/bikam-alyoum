import sqlite3
from datetime import datetime
import flet as ft

DB_NAME = "bikam_native.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT, icon TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS areas (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, unit TEXT, cat_id INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS prices (id INTEGER PRIMARY KEY AUTOINCREMENT, prod_id INTEGER, shop TEXT, area_id INTEGER, price REAL, updated_at TEXT)')

    if c.execute("SELECT COUNT(*) FROM categories").fetchone()[0] == 0:
        cats = [
            (1, 'مواد غذائية', '🛒'), (2, 'خضروات وفواكه', '🥬'), (3, 'ألبان ومخبوزات', '🥛'),
            (4, 'لحوم ودواجن', '🍗'), (5, 'أدوات منزلية', '🏠'), (6, 'إكسسوارات هواتف', '📱'),
            (7, 'مواد تنظيف', '🧼'), (8, 'ذهب وعملات', '🪙'), (9, 'غاز ومشتقات', '⛽')
        ]
        c.executemany('INSERT INTO categories VALUES (?, ?, ?)', cats)

        areas = [
            (1, 'صنعاء - حدة'), (2, 'صنعاء - التحرير'), (3, 'صنعاء - شميلة'),
            (4, 'صنعاء - السبعين'), (5, 'صنعاء - شعوب'), (6, 'ذمار - المدينة'),
            (7, 'ذمار - معبر'), (8, 'عدن - كريتر'), (9, 'تعز - المدينة'), (10, 'إب - المدينة')
        ]
        c.executemany('INSERT INTO areas VALUES (?, ?)', areas)

        prods = [
            ('صلصة طماطم (حبة صغيرة)', 'حبة 70 جرام', 1), ('دقيق السنابل أبيض', 'كيس 50 كجم', 1),
            ('دقيق أحمر بر مطحون', 'كيس 50 كجم', 1), ('أرز بسمتي مزة', 'كيس 10 كجم', 1),
            ('سكر ناعم', 'كيس 10 كجم', 1), ('زيت طبخ نباتي', 'دبة 4 لتر', 1),
            ('فاصوليا حمراء معلبة', 'علبة 400 جرام', 1), ('تونة قطعة واحدة', 'علبة 160 جرام', 1),
            ('شاي الكبوس خرز', 'عبوة 250 جرام', 1), ('بصل أحمر بلدي', 'كيلو', 2),
            ('طماطم بلدي طازج', 'كيلو', 2), ('بطاطس صنعاني / ذماري', 'كيلو', 2),
            ('موز بلدي طازج', 'كيلو', 2), ('تفاح أحمر', 'كيلو', 2),
            ('زبادي طازج (علبة)', 'علبة صغيرة', 3), ('حليب بودرة درجة أولى', 'كيلو', 3),
            ('خبز روتي (كيس)', 'كيس 6 حبات', 3), ('طبق بيض بلدي', 'طبق 30 حبة', 4),
            ('دجاج طازج مبرد', 'حبة 1 كجم', 4), ('لحم بقري بلدي صافي', 'كيلو', 4),
            ('ترمس شاي ستانلس 1 لتر', 'حبة', 5), ('طقم قدور طبخ ألمنيوم', 'طقم 4 قطع', 5),
            ('لمبة ليد موفرة 15 وات', 'حبة', 5), ('شاحن هاتف سريع 33 وات', 'حبة', 6),
            ('كيبل شحن Type-C أصلي', 'حبة', 6), ('سماعة بلوتوث لاسلكية', 'حبة', 6),
            ('صابون غسيل ملابس', 'كيس 1.5 كجم', 7), ('سائل غسيل صحون 750 مل', 'عبوة', 7),
            ('ذهب عيار 21 (صنعاء)', 'جرام', 8), ('اسطوانة غاز منزلي', 'اسطوانة', 9),
            ('بترول (دبة 20 لتر)', '20 لتر', 9), ('ديزل (دبة 20 لتر)', '20 لتر', 9)
        ]
        c.executemany('INSERT INTO products (name, unit, cat_id) VALUES (?, ?, ?)', prods)

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        prices = [
            (1, 'بقالة الأمانة', 1, 50, now), (1, 'سوبر ماركت ذمار', 6, 50, now),
            (2, 'جملة شميلة', 3, 15000, now), (2, 'أسواق ذمار المركزية', 6, 15200, now),
            (3, 'مطحنة التحرير', 2, 13000, now), (4, 'هايبر المستهلك', 4, 7400, now),
            (5, 'جملة شميلة', 3, 4100, now), (6, 'سوبر ماركت الهدى', 1, 4600, now),
            (7, 'بقالة الخير', 5, 320, now), (8, 'سوبر ماركت الهدى', 1, 450, now),
            (9, 'تموينات السعادة', 2, 900, now), (10, 'سوق شميلة المركزي', 3, 350, now),
            (11, 'سوق التحرير', 2, 400, now), (12, 'سوق ذمار المركزي', 6, 350, now),
            (13, 'سوق التحرير', 2, 500, now), (14, 'خضروات حدة', 1, 1200, now),
            (15, 'بقالة الأمانة', 1, 150, now), (16, 'هايبر المستهلك', 4, 2800, now),
            (17, 'مخبز الأمانة', 1, 250, now), (18, 'جملة شميلة', 3, 1350, now),
            (19, 'دواجن الوطنية', 5, 1750, now), (20, 'ملاحم البركة', 1, 4500, now),
            (21, 'معرض الأدوات المنزلية', 2, 3500, now), (22, 'أسواق شميلة', 3, 12500, now),
            (23, 'كهربائيات التحرير', 2, 600, now), (24, 'مركز اتصالات حدة', 1, 3500, now),
            (25, 'إكسسوارات التحرير', 2, 1200, now), (26, 'عالم الجوالات', 1, 4500, now),
            (27, 'هايبر المستهلك', 4, 1600, now), (28, 'سوبر ماركت الهدى', 1, 850, now),
            (29, 'صاغة التحرير', 2, 62112, now), (30, 'وكيل الغاز الرسمي', 1, 7500, now),
            (31, 'شركة النفط', 4, 11400, now), (32, 'شركة النفط', 4, 13000, now)
        ]
        c.executemany('INSERT INTO prices (prod_id, shop, area_id, price, updated_at) VALUES (?, ?, ?, ?, ?)', prices)

    conn.commit()
    conn.close()

def main(page: ft.Page):
    init_db()
    page.title = "بكم اليوم؟"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F1F5F9"
    page.padding = 0

    selected_cat = 0
    selected_area = 0
    search_query = ""

    def get_data():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cats = conn.execute("SELECT * FROM categories").fetchall()
        areas = conn.execute("SELECT * FROM areas").fetchall()

        sql = """
            SELECT p.id, p.name, p.unit, p.cat_id, c.name as cname, c.icon as cicon,
                   MIN(pr.price) as min_p, MAX(pr.price) as max_p, AVG(pr.price) as avg_p,
                   MAX(pr.updated_at) as upd
            FROM products p
            JOIN categories c ON p.cat_id = c.id
            JOIN prices pr ON pr.prod_id = p.id
            WHERE 1=1
        """
        params = []
        if search_query:
            sql += " AND p.name LIKE ?"
            params.append(f"%{search_query}%")
        if selected_cat > 0:
            sql += " AND p.cat_id = ?"
            params.append(selected_cat)
        if selected_area > 0:
            sql += " AND pr.area_id = ?"
            params.append(selected_area)

        sql += " GROUP BY p.id ORDER BY upd DESC"
        prods = []
        for r in conn.execute(sql, params).fetchall():
            d = dict(r)
            s_sql = "SELECT pr.shop, pr.price, a.name as aname FROM prices pr JOIN areas a ON pr.area_id = a.id WHERE pr.prod_id = ?"
            s_p = [r["id"]]
            if selected_area > 0:
                s_sql += " AND pr.area_id = ?"
                s_p.append(selected_area)
            d["shops"] = [dict(s) for s in conn.execute(s_sql + " ORDER BY pr.price ASC", s_p).fetchall()]
            prods.append(d)
        conn.close()
        return cats, areas, prods

    products_list = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)
    cats_row = ft.Row(scroll=ft.ScrollMode.AUTO, spacing=8)

    def open_add_dialog(prefill_name="", prefill_unit="", prefill_cat=1):
        name_field = ft.TextField(label="اسم السلعة", value=prefill_name, read_only=bool(prefill_name))
        unit_field = ft.TextField(label="العبوة / الوزن", value=prefill_unit, read_only=bool(prefill_unit))
        price_field = ft.TextField(label="السعر بالريال اليمني", keyboard_type=ft.KeyboardType.NUMBER)
        shop_field = ft.TextField(label="اسم المحل أو السوق")

        cats, areas, _ = get_data()
        cat_dd = ft.Dropdown(
            label="التصنيف",
            value=str(prefill_cat),
            options=[ft.dropdown.Option(str(c["id"]), f"{c['icon']} {c['name']}") for c in cats]
        )
        area_dd = ft.Dropdown(
            label="المنطقة / المحافظة",
            value="1",
            options=[ft.dropdown.Option(str(a["id"]), a["name"]) for a in areas]
        )

        def save_price(e):
            if not (name_field.value and unit_field.value and price_field.value and shop_field.value):
                return
            try:
                val = float(price_field.value)
                if val <= 0: return
            except:
                return

            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            ex = cur.execute("SELECT id FROM products WHERE name=? AND unit=?", (name_field.value.strip(), unit_field.value.strip())).fetchone()
            pid = ex[0] if ex else cur.execute("INSERT INTO products (name, unit, cat_id) VALUES (?, ?, ?)", (name_field.value.strip(), unit_field.value.strip(), int(cat_dd.value))).lastrowid
            cur.execute("INSERT INTO prices (prod_id, shop, area_id, price, updated_at) VALUES (?, ?, ?, ?, ?)",
                        (pid, shop_field.value.strip(), int(area_dd.value), val, datetime.now().strftime("%Y-%m-%d %H:%M")))
            conn.commit()
            conn.close()
            page.close(dlg)
            refresh_ui()
            page.open(ft.SnackBar(ft.Text("تم حفظ السعر بنجاح!"), bgcolor="#16A34A"))

        dlg = ft.AlertDialog(
            title=ft.Text("تحديث / إضافة سعر", weight=ft.FontWeight.BOLD),
            content=ft.Column([name_field, unit_field, cat_dd, price_field, shop_field, area_dd], tight=True, scroll=ft.ScrollMode.AUTO),
            actions=[
                ft.TextButton("إلغاء", on_click=lambda e: page.close(dlg)),
                ft.ElevatedButton("حفظ السعر", bgcolor="#0F766E", color="white", on_click=save_price)
            ]
        )
        page.open(dlg)

    def refresh_ui():
        nonlocal selected_cat
        cats, areas, prods = get_data()

        cats_row.controls.clear()
        cats_row.controls.append(
            ft.ElevatedButton("🌐 الكل", bgcolor="#0F766E" if selected_cat == 0 else "white",
                              color="white" if selected_cat == 0 else "#1E293B",
                              on_click=lambda e: set_cat(0))
        )
        for c in cats:
            cid = c["id"]
            cats_row.controls.append(
                ft.ElevatedButton(f"{c['icon']} {c['name']}",
                                  bgcolor="#0F766E" if selected_cat == cid else "white",
                                  color="white" if selected_cat == cid else "#1E293B",
                                  on_click=lambda e, x=cid: set_cat(x))
            )

        products_list.controls.clear()
        for p in prods:
            shops_col = ft.Column([
                ft.Row([
                    ft.Text(f"🏪 {s['shop']} ({s['aname']})", size=13),
                    ft.Text(f"{s['price']:,.0f} ريال", weight=ft.FontWeight.BOLD, color="#0F766E")
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN) for s in p["shops"]
            ], spacing=4)

            card = ft.Container(
                bgcolor="white", border_radius=14, padding=14,
                border=ft.border.all(1, "#E2E8F0"),
                content=ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text(p["name"], size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(f"{p['cicon']} {p['cname']} • {p['unit']}", size=12, color="#64748B")
                        ], expand=True),
                        ft.OutlinedButton("+ حدّث", on_click=lambda e, n=p["name"], u=p["unit"], c=p["cat_id"]: open_add_dialog(n, u, c))
                    ]),
                    ft.Row([
                        ft.Container(bgcolor="#E0F2FE", padding=8, border_radius=8, expand=True,
                                     content=ft.Column([ft.Text("أقل سعر", size=11, color="#0284C7"), ft.Text(f"{p['min_p']:,.0f} ر.ي", weight=ft.FontWeight.BOLD, color="#0284C7")], horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                        ft.Container(bgcolor="#FEE2E2", padding=8, border_radius=8, expand=True,
                                     content=ft.Column([ft.Text("أعلى سعر", size=11, color="#DC2626"), ft.Text(f"{p['max_p']:,.0f} ر.ي", weight=ft.FontWeight.BOLD, color="#DC2626")], horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                        ft.Container(bgcolor="#DCFCE7", padding=8, border_radius=8, expand=True,
                                     content=ft.Column([ft.Text("المتوسط", size=11, color="#16A34A"), ft.Text(f"{p['avg_p']:,.0f} ر.ي", weight=ft.FontWeight.BOLD, color="#16A34A")], horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                    ], spacing=6),
                    ft.ExpansionTile(title=ft.Text(f"المحلات ({len(p['shops'])}) • 🕒 {p['upd']}", size=12, color="#64748B"), controls=[shops_col])
                ], spacing=8)
            )
            products_list.controls.append(card)
        page.update()

    def set_cat(cid):
        nonlocal selected_cat
        selected_cat = cid
        refresh_ui()

    def on_search(e):
        nonlocal search_query
        search_query = e.control.value.strip()
        refresh_ui()

    def on_area_change(e):
        nonlocal selected_area
        selected_area = int(e.control.value)
        refresh_ui()

    _, init_areas, _ = get_data()
    area_filter = ft.Dropdown(
        value="0", on_change=on_area_change, bgcolor="white", border_radius=10,
        options=[ft.dropdown.Option("0", "📍 كل المحافظات والمناطق (صنعاء، ذمار، عدن...)")] +
                [ft.dropdown.Option(str(a["id"]), f"📍 {a['name']}") for a in init_areas]
    )

    header = ft.Container(
        bgcolor="#0F766E", padding=ft.padding.only(top=35, bottom=16, left=16, right=16),
        border_radius=ft.border_radius.only(bottom_left=18, bottom_right=18),
        content=ft.Column([
            ft.Text("💰 بكم اليوم؟", size=22, weight=ft.FontWeight.BOLD, color="white"),
            ft.Text("دليل أسعار الأسواق اليمنية - تطبيق أندرويد", size=12, color="#CCFBF1")
        ])
    )

    body = ft.Container(
        padding=12, expand=True,
        content=ft.Column([
            ft.TextField(hint_text="ابحث عن أي سلعة (صلصة، دقيق، ذهب، شاحن...)", bgcolor="white", border_radius=12, on_change=on_search),
            cats_row,
            area_filter,
            products_list
        ], spacing=10, expand=True)
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, text="إضافة سعر", bgcolor="#0F766E", foreground_color="white",
        on_click=lambda e: open_add_dialog()
    )

    page.add(header, body)
    refresh_ui()

ft.app(target=main)
