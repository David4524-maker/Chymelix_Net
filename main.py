import flet as ft
import random
import threading
import time
import base64

# ============================================================
#  CHYMELIX NET — Versión Python (Flet)
#  Simulación local de Seguridad, Rendimiento y Entrega
# ============================================================

# ============ DICCIONARIO i18n (10 idiomas) ============
I18N = {
    "es": dict(
        tagline="Seguridad · Rendimiento · Entrega",
        nav_dashboard="Panel", nav_security="Seguridad", nav_performance="Rendimiento",
        nav_delivery="Entregas", nav_settings="Ajustes",
        dash_title="Panel de control", dash_sub="Estado global de tu red en tiempo real",
        security_score="Índice de seguridad", performance_score="Índice de rendimiento",
        delivery_rate="Tasa de entrega", active_threats="Amenazas activas",
        sys_status="Estado del sistema", live="EN VIVO",
        security_title="Centro de seguridad", security_sub="Escaneo, blindaje y respuesta",
        run_scan="Ejecutar escaneo", scanning="Escaneando…", scan_done="Escaneo completado",
        firewall="Cortafuegos", encryption="Cifrado AES-256", auth="Autenticación 2FA",
        threats_blocked="Amenazas bloqueadas", last_scan="Último escaneo",
        enabled="Activado", disabled="Desactivado",
        performance_title="Rendimiento", performance_sub="Métricas en directo",
        cpu="CPU", memory="Memoria", network="Red", latency="Latencia",
        uptime="Disponibilidad", requests="Solicitudes/s",
        delivery_title="Centro de entregas", delivery_sub="Seguimiento de paquetes",
        packages="Paquetes", in_transit="En tránsito", delivered="Entregados", pending="Pendientes",
        tracking_id="Seguimiento", status="Estado",
        settings_title="Ajustes", language="Idioma", notifications="Notificaciones",
        auto_scan="Escaneo automático", save="Guardar", saved="Guardado ✓",
        footer="Plataforma local de seguridad, rendimiento y entrega",
        healthy="Óptimo", warning="Atención", critical="Crítico",
    ),
    "en": dict(
        tagline="Security · Performance · Delivery",
        nav_dashboard="Dashboard", nav_security="Security", nav_performance="Performance",
        nav_delivery="Delivery", nav_settings="Settings",
        dash_title="Control panel", dash_sub="Global network status in real time",
        security_score="Security score", performance_score="Performance score",
        delivery_rate="Delivery rate", active_threats="Active threats",
        sys_status="System status", live="LIVE",
        security_title="Security center", security_sub="Scanning, hardening and response",
        run_scan="Run scan", scanning="Scanning…", scan_done="Scan completed",
        firewall="Firewall", encryption="AES-256 encryption", auth="2FA authentication",
        threats_blocked="Threats blocked", last_scan="Last scan",
        enabled="Enabled", disabled="Disabled",
        performance_title="Performance", performance_sub="Live metrics",
        cpu="CPU", memory="Memory", network="Network", latency="Latency",
        uptime="Uptime", requests="Requests/s",
        delivery_title="Delivery center", delivery_sub="Package tracking",
        packages="Packages", in_transit="In transit", delivered="Delivered", pending="Pending",
        tracking_id="Tracking ID", status="Status",
        settings_title="Settings", language="Language", notifications="Notifications",
        auto_scan="Auto scan", save="Save", saved="Saved ✓",
        footer="Local security, performance and delivery platform",
        healthy="Healthy", warning="Warning", critical="Critical",
    ),
    "fr": dict(
        tagline="Sécurité · Performance · Livraison",
        nav_dashboard="Tableau", nav_security="Sécurité", nav_performance="Performance",
        nav_delivery="Livraisons", nav_settings="Réglages",
        dash_title="Panneau de contrôle", dash_sub="État global du réseau en temps réel",
        security_score="Indice de sécurité", performance_score="Indice de performance",
        delivery_rate="Taux de livraison", active_threats="Menaces actives",
        sys_status="État du système", live="EN DIRECT",
        security_title="Centre de sécurité", security_sub="Analyse, blindage et réponse",
        run_scan="Lancer l'analyse", scanning="Analyse en cours…", scan_done="Analyse terminée",
        firewall="Pare-feu", encryption="Chiffrement AES-256", auth="Authentification 2FA",
        threats_blocked="Menaces bloquées", last_scan="Dernière analyse",
        enabled="Activé", disabled="Désactivé",
        performance_title="Performance", performance_sub="Métriques en direct",
        cpu="Processeur", memory="Mémoire", network="Réseau", latency="Latence",
        uptime="Disponibilité", requests="Requêtes/s",
        delivery_title="Centre de livraison", delivery_sub="Suivi des colis",
        packages="Colis", in_transit="En transit", delivered="Livrés", pending="En attente",
        tracking_id="N° de suivi", status="Statut",
        settings_title="Réglages", language="Langue", notifications="Notifications",
        auto_scan="Analyse automatique", save="Enregistrer", saved="Enregistré ✓",
        footer="Plateforme locale de sécurité, performance et livraison",
        healthy="Optimal", warning="Attention", critical="Critique",
    ),
    "de": dict(
        tagline="Sicherheit · Leistung · Lieferung",
        nav_dashboard="Übersicht", nav_security="Sicherheit", nav_performance="Leistung",
        nav_delivery="Lieferungen", nav_settings="Einstellungen",
        dash_title="Kontrollpanel", dash_sub="Globaler Netzwerkstatus in Echtzeit",
        security_score="Sicherheitsindex", performance_score="Leistungsindex",
        delivery_rate="Lieferquote", active_threats="Aktive Bedrohungen",
        sys_status="Systemstatus", live="LIVE",
        security_title="Sicherheitszentrum", security_sub="Scan, Härtung und Abwehr",
        run_scan="Scan starten", scanning="Scan läuft…", scan_done="Scan abgeschlossen",
        firewall="Firewall", encryption="AES-256-Verschlüsselung", auth="2FA-Authentifizierung",
        threats_blocked="Blockierte Bedrohungen", last_scan="Letzter Scan",
        enabled="Aktiviert", disabled="Deaktiviert",
        performance_title="Leistung", performance_sub="Live-Metriken",
        cpu="CPU", memory="Speicher", network="Netzwerk", latency="Latenz",
        uptime="Verfügbarkeit", requests="Anfragen/s",
        delivery_title="Lieferzentrum", delivery_sub="Paketverfolgung",
        packages="Pakete", in_transit="Unterwegs", delivered="Zugestellt", pending="Ausstehend",
        tracking_id="Sendungsnummer", status="Status",
        settings_title="Einstellungen", language="Sprache", notifications="Benachrichtigungen",
        auto_scan="Automatischer Scan", save="Speichern", saved="Gespeichert ✓",
        footer="Lokale Plattform für Sicherheit, Leistung und Lieferung",
        healthy="Optimal", warning="Achtung", critical="Kritisch",
    ),
    "pt": dict(
        tagline="Segurança · Desempenho · Entrega",
        nav_dashboard="Painel", nav_security="Segurança", nav_performance="Desempenho",
        nav_delivery="Entregas", nav_settings="Ajustes",
        dash_title="Painel de controle", dash_sub="Estado da rede em tempo real",
        security_score="Índice de segurança", performance_score="Índice de desempenho",
        delivery_rate="Taxa de entrega", active_threats="Ameaças ativas",
        sys_status="Estado do sistema", live="AO VIVO",
        security_title="Centro de segurança", security_sub="Varredura e resposta",
        run_scan="Executar varredura", scanning="Verificando…", scan_done="Varredura concluída",
        firewall="Firewall", encryption="Criptografia AES-256", auth="Autenticação 2FA",
        threats_blocked="Ameaças bloqueadas", last_scan="Última varredura",
        enabled="Ativado", disabled="Desativado",
        performance_title="Desempenho", performance_sub="Métricas ao vivo",
        cpu="CPU", memory="Memória", network="Rede", latency="Latência",
        uptime="Disponibilidade", requests="Requisições/s",
        delivery_title="Centro de entregas", delivery_sub="Rastreamento de pacotes",
        packages="Pacotes", in_transit="Em trânsito", delivered="Entregues", pending="Pendentes",
        tracking_id="Rastreio", status="Status",
        settings_title="Ajustes", language="Idioma", notifications="Notificações",
        auto_scan="Varredura automática", save="Salvar", saved="Salvo ✓",
        footer="Plataforma local de segurança, desempenho e entrega",
        healthy="Ótimo", warning="Atenção", critical="Crítico",
    ),
    "it": dict(
        tagline="Sicurezza · Prestazioni · Consegna",
        nav_dashboard="Pannello", nav_security="Sicurezza", nav_performance="Prestazioni",
        nav_delivery="Consegne", nav_settings="Impostazioni",
        dash_title="Pannello di controllo", dash_sub="Stato globale della rete in tempo reale",
        security_score="Indice di sicurezza", performance_score="Indice di prestazioni",
        delivery_rate="Tasso di consegna", active_threats="Minacce attive",
        sys_status="Stato del sistema", live="IN DIRETTA",
        security_title="Centro sicurezza", security_sub="Scansione e risposta",
        run_scan="Avvia scansione", scanning="Scansione…", scan_done="Scansione completata",
        firewall="Firewall", encryption="Crittografia AES-256", auth="Autenticazione 2FA",
        threats_blocked="Minacce bloccate", last_scan="Ultima scansione",
        enabled="Attivo", disabled="Disattivo",
        performance_title="Prestazioni", performance_sub="Metriche in diretta",
        cpu="CPU", memory="Memoria", network="Rete", latency="Latenza",
        uptime="Disponibilità", requests="Richieste/s",
        delivery_title="Centro consegne", delivery_sub="Tracciamento pacchi",
        packages="Pacchi", in_transit="In transito", delivered="Consegnati", pending="In attesa",
        tracking_id="Tracciamento", status="Stato",
        settings_title="Impostazioni", language="Lingua", notifications="Notifiche",
        auto_scan="Scansione automatica", save="Salva", saved="Salvato ✓",
        footer="Piattaforma locale per sicurezza, prestazioni e consegna",
        healthy="Ottimo", warning="Attenzione", critical="Critico",
    ),
    "ru": dict(
        tagline="Безопасность · Производительность · Доставка",
        nav_dashboard="Панель", nav_security="Безопасность", nav_performance="Производительность",
        nav_delivery="Доставка", nav_settings="Настройки",
        dash_title="Панель управления", dash_sub="Состояние сети в реальном времени",
        security_score="Индекс безопасности", performance_score="Индекс производительности",
        delivery_rate="Доля доставок", active_threats="Активные угрозы",
        sys_status="Состояние системы", live="В ЭФИРЕ",
        security_title="Центр безопасности", security_sub="Сканирование и защита",
        run_scan="Запустить сканирование", scanning="Сканирование…", scan_done="Сканирование завершено",
        firewall="Межсетевой экран", encryption="Шифрование AES-256", auth="Двухфакторная аутентификация",
        threats_blocked="Угроз заблокировано", last_scan="Последнее сканирование",
        enabled="Включено", disabled="Отключено",
        performance_title="Производительность", performance_sub="Метрики в реальном времени",
        cpu="ЦП", memory="Память", network="Сеть", latency="Задержка",
        uptime="Доступность", requests="Запросов/с",
        delivery_title="Центр доставки", delivery_sub="Отслеживание посылок",
        packages="Посылки", in_transit="В пути", delivered="Доставлено", pending="В ожидании",
        tracking_id="Отслеживание", status="Статус",
        settings_title="Настройки", language="Язык", notifications="Уведомления",
        auto_scan="Автосканирование", save="Сохранить", saved="Сохранено ✓",
        footer="Локальная платформа безопасности, производительности и доставки",
        healthy="Отлично", warning="Внимание", critical="Критично",
    ),
    "zh": dict(
        tagline="安全 · 性能 · 配送",
        nav_dashboard="仪表板", nav_security="安全", nav_performance="性能",
        nav_delivery="配送", nav_settings="设置",
        dash_title="控制面板", dash_sub="实时监控网络状态",
        security_score="安全指数", performance_score="性能指数",
        delivery_rate="配送率", active_threats="活跃威胁",
        sys_status="系统状态", live="实时",
        security_title="安全中心", security_sub="扫描、防护与响应",
        run_scan="开始扫描", scanning="正在扫描…", scan_done="扫描完成",
        firewall="防火墙", encryption="AES-256 加密", auth="双重认证",
        threats_blocked="已拦截威胁", last_scan="上次扫描",
        enabled="已启用", disabled="已禁用",
        performance_title="性能", performance_sub="实时指标",
        cpu="处理器", memory="内存", network="网络", latency="延迟",
        uptime="在线率", requests="请求/秒",
        delivery_title="配送中心", delivery_sub="包裹跟踪",
        packages="包裹", in_transit="运输中", delivered="已送达", pending="待处理",
        tracking_id="跟踪编号", status="状态",
        settings_title="设置", language="语言", notifications="通知",
        auto_scan="自动扫描", save="保存", saved="已保存 ✓",
        footer="本地安全、性能与配送平台",
        healthy="良好", warning="注意", critical="严重",
    ),
    "ja": dict(
        tagline="セキュリティ · パフォーマンス · デリバリー",
        nav_dashboard="ダッシュボード", nav_security="セキュリティ", nav_performance="パフォーマンス",
        nav_delivery="デリバリー", nav_settings="設定",
        dash_title="コントロールパネル", dash_sub="ネットワーク状態をリアルタイム監視",
        security_score="セキュリティ指数", performance_score="パフォーマンス指数",
        delivery_rate="配達率", active_threats="アクティブな脅威",
        sys_status="システム状態", live="ライブ",
        security_title="セキュリティセンター", security_sub="スキャンと防御",
        run_scan="スキャン実行", scanning="スキャン中…", scan_done="スキャン完了",
        firewall="ファイアウォール", encryption="AES-256 暗号化", auth="二段階認証",
        threats_blocked="ブロックした脅威", last_scan="最終スキャン",
        enabled="有効", disabled="無効",
        performance_title="パフォーマンス", performance_sub="リアルタイム指標",
        cpu="CPU", memory="メモリ", network="ネットワーク", latency="レイテンシ",
        uptime="稼働率", requests="リクエスト/秒",
        delivery_title="デリバリーセンター", delivery_sub="荷物の追跡",
        packages="荷物", in_transit="輸送中", delivered="配達済み", pending="保留中",
        tracking_id="追跡番号", status="ステータス",
        settings_title="設定", language="言語", notifications="通知",
        auto_scan="自動スキャン", save="保存", saved="保存しました ✓",
        footer="ローカル版セキュリティ・パフォーマンス・デリバリープラットフォーム",
        healthy="良好", warning="注意", critical="危険",
    ),
    "ar": dict(
        tagline="الأمان · الأداء · التسليم",
        nav_dashboard="لوحة التحكم", nav_security="الأمان", nav_performance="الأداء",
        nav_delivery="التسليم", nav_settings="الإعدادات",
        dash_title="لوحة التحكم", dash_sub="حالة الشبكة في الوقت الحقيقي",
        security_score="مؤشر الأمان", performance_score="مؤشر الأداء",
        delivery_rate="معدل التسليم", active_threats="التهديدات النشطة",
        sys_status="حالة النظام", live="مباشر",
        security_title="مركز الأمان", security_sub="الفحص والحماية",
        run_scan="بدء الفحص", scanning="جارٍ الفحص…", scan_done="اكتمل الفحص",
        firewall="جدار الحماية", encryption="تشفير AES-256", auth="المصادقة الثنائية",
        threats_blocked="التهديدات المحجوبة", last_scan="آخر فحص",
        enabled="مُفعّل", disabled="مُعطّل",
        performance_title="الأداء", performance_sub="مقاييس مباشرة",
        cpu="المعالج", memory="الذاكرة", network="الشبكة", latency="زمن الاستجابة",
        uptime="وقت التشغيل", requests="طلبات/ث",
        delivery_title="مركز التسليم", delivery_sub="تتبع الطرود",
        packages="الطرود", in_transit="قيد النقل", delivered="تم التسليم", pending="قيد الانتظار",
        tracking_id="رقم التتبع", status="الحالة",
        settings_title="الإعدادات", language="اللغة", notifications="الإشعارات",
        auto_scan="فحص تلقائي", save="حفظ", saved="تم الحفظ ✓",
        footer="منصة محلية للأمان والأداء والتسليم",
        healthy="ممتاز", warning="تحذير", critical="حرج",
    ),
}

LANGS = [("es", "Español"), ("en", "English"), ("fr", "Français"),
         ("de", "Deutsch"), ("pt", "Português"), ("it", "Italiano"),
         ("ru", "Русский"), ("zh", "中文"), ("ja", "日本語"), ("ar", "العربية")]

# ============ LOGO SVG (recreado de la imagen) ============
LOGO_SVG = """<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
<path d="M 25 50 C 25 5, 95 5, 95 50" fill="none" stroke="#000000" stroke-width="12" stroke-linecap="round"/>
<path d="M 25 35 L 95 35 L 95 75 C 95 100, 60 115, 60 115 C 60 115, 25 100, 25 75 Z" fill="#00b4ff" stroke="#ff0000" stroke-width="10" stroke-linejoin="round"/>
<path d="M 50 45 h 20 v 15 h 15 v 20 h -15 v 15 h -20 v -15 h -15 v -20 h 15 z" fill="#d4d4d4" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
<path d="M 60 50 v 40 M 40 70 h 40" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
<rect x="8" y="55" width="24" height="38" rx="10" fill="#000000"/>
<rect x="88" y="55" width="24" height="38" rx="10" fill="#000000"/>
<path d="M 88 70 C 75 70, 75 70, 65 70" fill="none" stroke="#000000" stroke-width="14" stroke-linecap="round"/>
<circle cx="65" cy="70" r="14" fill="#000000"/>
</svg>"""
LOGO_URI = "data:image/svg+xml;base64," + base64.b64encode(LOGO_SVG.encode()).decode()

# ============ Paleta de colores ============
BLUE_900 = "#061a3f"
BLUE_800 = "#0a2a6b"
BLUE_700 = "#0f3d91"
BLUE_600 = "#1565c0"
BLUE_500 = "#2b7be4"
BLUE_100 = "#e4eefc"
BLUE_50  = "#f2f7fe"
RED_700  = "#a5161d"
RED_600  = "#d32029"
RED_500  = "#e53935"
RED_100  = "#fdeaea"
WHITE    = "#ffffff"
INK      = "#0b1a33"
MUTED    = "#5f7191"
BG       = "#eef3fa"
LINE     = "#dbe6f5"

CITIES = ["Madrid", "Bogotá", "CDMX", "Lima", "Buenos Aires",
          "Santiago", "Miami", "Lisboa", "Berlín", "Tokio"]

THREAT_POOL = ["Port scan", "Brute force SSH", "Malformed packet",
               "Suspicious DNS query", "Outdated TLS cipher", "Unknown device"]


# ============================================================
#  APLICACIÓN
# ============================================================
class ChymelixApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang = "es"
        self.current_view = "dashboard"
        self.refs = {}          # referencias a controles dinámicos
        self.scanning = False

        self.security = dict(firewall=True, encryption=True, auth=True, blocked=1247, threats=2)
        self.perf = dict(cpu=34.0, mem=58.0, net=42.0, latency=18.0, uptime=99.98, rps=1240)
        self.history = dict(
            cpu=[random.uniform(20, 55) for _ in range(30)],
            mem=[random.uniform(40, 70) for _ in range(30)],
        )
        self.packages = self._make_packages(6)

        self._setup_page()
        self._build_ui()
        self._start_loops()

    # -------- helpers --------
    def t(self, key: str) -> str:
        return I18N.get(self.lang, I18N["en"]).get(key, I18N["en"].get(key, key))

    def _make_packages(self, n):
        out = []
        for _ in range(n):
            prog = random.randint(0, 100)
            out.append(dict(
                id="CHX-" + "".join(random.choice("ABCDEFGHJKLMNPQRSTUVWXYZ0123456789") for _ in range(8)),
                dest=random.choice(CITIES), progress=prog,
            ))
        return out

    def _setup_page(self):
        p = self.page
        p.title = "Chymelix Net"
        p.bgcolor = BG
        p.padding = 0
        p.spacing = 0
        p.window_width = 1240
        p.window_height = 860

    # -------- UI principal --------
    def _build_ui(self):
        self.page.controls.clear()

        topbar = self._build_topbar()
        navbar = self._build_navbar()
        self.content = ft.Container(expand=True, padding=ft.padding.symmetric(horizontal=22, vertical=18))
        self._render_view(self.current_view)
        footer = self._build_footer()

        self.page.add(ft.Column([topbar, navbar, self.content, footer], expand=True, spacing=0))
        self.page.update()

    def _render_view(self, name):
        self.current_view = name
        builder = getattr(self, f"_build_{name}")
        self.content.content = ft.Column([builder()], scroll=ft.ScrollMode.AUTO, expand=True)
        self.page.update()

    def _change_lang(self, e):
        self.lang = e.control.value
        self._build_ui()

    def _nav_to(self, name):
        self._render_view(name)

    # -------- TOPBAR --------
    def _build_topbar(self):
        lang_dd = ft.Dropdown(
            options=[ft.dropdown.Option(code, name) for code, name in LANGS],
            value=self.lang, width=140, text_size=12,
            border_color=WHITE, text_style=ft.TextStyle(color=WHITE),
            fill_color="rgba(255,255,255,0.1)", filled=True,
            on_change=self._change_lang, border_radius=9,
            content_padding=ft.padding.symmetric(horizontal=10, vertical=2),
        )

        self.clock_text = ft.Text("--:--:--", size=13, color=WHITE, weight=ft.FontWeight.W_600)

        brand = ft.Row([
            ft.Image(src=LOGO_URI, width=52, height=52),
            ft.Column([
                ft.Text("Chymelix Net", size=18, weight=ft.FontWeight.BOLD, color=WHITE),
                ft.Text(self.t("tagline"), size=10, color="#8fb8ee"),
            ], spacing=0, alignment=ft.MainAxisAlignment.CENTER),
        ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        live_pill = ft.Container(
            content=ft.Row([
                ft.Container(width=8, height=8, bgcolor=RED_500, border_radius=4),
                ft.Text(self.t("live"), size=10, color="#ffb3b6", weight=ft.FontWeight.BOLD),
            ], spacing=6, tight=True),
            padding=ft.padding.symmetric(horizontal=11, vertical=5),
            border=ft.border.all(1, "rgba(229,57,53,0.55)"),
            border_radius=99, bgcolor="rgba(229,57,53,0.16)",
        )

        right = ft.Row([live_pill, self.clock_text, lang_dd],
                       spacing=10, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        return ft.Container(
            content=ft.Row([brand, right], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                           vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.padding.symmetric(horizontal=22, vertical=12),
            gradient=ft.LinearGradient(begin=ft.alignment.center_left, end=ft.alignment.center_right,
                                       colors=[BLUE_900, BLUE_800, BLUE_700]),
            border=ft.border.only(bottom=ft.BorderSide(3, RED_600)),
        )

    # -------- NAVBAR --------
    def _build_navbar(self):
        items = [
            ("dashboard",   "nav_dashboard",   ft.Icons.DASHBOARD),
            ("security",    "nav_security",    ft.Icons.SECURITY),
            ("performance", "nav_performance", ft.Icons.SPEED),
            ("delivery",    "nav_delivery",    ft.Icons.LOCAL_SHIPPING),
            ("settings",    "nav_settings",    ft.Icons.SETTINGS),
        ]
        btns = []
        for key, label_key, icon in items:
            active = (key == self.current_view)
            btns.append(ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(icon, size=16, color=WHITE if active else MUTED),
                    ft.Text(self.t(label_key), size=13,
                            color=WHITE if active else MUTED,
                            weight=ft.FontWeight.W_600),
                ], spacing=6, tight=True),
                style=ft.ButtonStyle(
                    bgcolor=BLUE_700 if active else WHITE,
                    color=WHITE if active else MUTED,
                    padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    shape=ft.RoundedRectangleBorder(radius=99),
                    elevation=0,
                    side=ft.BorderSide(0, "transparent") if active else ft.BorderSide(1, LINE),
                ),
                on_click=lambda e, k=key: self._nav_to(k),
            ))
        return ft.Container(
            content=ft.Row(btns, spacing=8, wrap=True),
            padding=ft.padding.only(left=22, right=22, top=14),
        )

    # -------- FOOTER --------
    def _build_footer(self):
        return ft.Container(
            content=ft.Row([
                ft.Text(f"Chymelix Net — {self.t('footer')}", size=12, color=MUTED),
                ft.Text("SECURE · FAST · DELIVERED", size=12, color=RED_600,
                        weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=ft.padding.symmetric(horizontal=22, vertical=18),
            border=ft.border.only(top=ft.BorderSide(2, LINE)),
        )

    # -------- helpers de tarjetas --------
    def _card(self, content, accent_red=False):
        return ft.Container(
            content=ft.Column([content], spacing=6),
            padding=18, bgcolor=WHITE, border_radius=16,
            border=ft.border.all(1, LINE),
            left_border=None,
            shadow=ft.BoxShadow(blur_radius=8, color="rgba(11,26,51,0.06)"),
        )

    def _stat(self, label, value_ctrl, sub, tag_text, tag_red=False):
        tag = ft.Container(
            content=ft.Text(tag_text, size=10, weight=ft.FontWeight.BOLD,
                            color=RED_700 if tag_red else BLUE_700),
            bgcolor=RED_100 if tag_red else BLUE_100,
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=99,
        )
        return ft.Column([
            ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color=MUTED),
            value_ctrl,
            ft.Text(sub, size=11, color=MUTED),
            tag,
        ], spacing=6, alignment=ft.MainAxisAlignment.START)

    def _gauge(self, key, pct, color=BLUE_600):
        """Devuelve un ProgressRing con el número centrado."""
        ring = ft.ProgressRing(value=pct / 100, width=132, height=132,
                               stroke_width=11, color=color, bgcolor=BLUE_100)
        num = ft.Text(f"{int(pct)}%", size=24, weight=ft.FontWeight.BOLD, color=BLUE_800)
        stack = ft.Stack([
            ring,
            ft.Container(content=num, width=132, height=132, alignment=ft.alignment.center),
        ], width=132, height=132)
        self.refs[f"gauge_{key}_ring"] = ring
        self.refs[f"gauge_{key}_num"] = num
        return stack

    def _sparkline(self, values, color, width=1100, height=110):
        """Sparkline simple basada en barras."""
        vmax = 100.0
        bars = []
        for v in values[-40:]:
            h = max(int(v / vmax * height), 2)
            bars.append(ft.Container(width=18, height=h, bgcolor=color,
                                     border_radius=ft.border_radius.only(top_left=3, top_right=3)))
        return ft.Container(
            content=ft.Row(bars, spacing=3,
                           vertical_alignment=ft.CrossAxisAlignment.END),
            width=width, height=height + 4,
            padding=ft.padding.only(top=4),
            border=ft.border.only(bottom=ft.BorderSide(1, LINE)),
        )

    # ========================================================
    #  VISTA: DASHBOARD
    # ========================================================
    def _build_dashboard(self):
        # KPIs
        self.refs["kpi_security"] = ft.Text("0%", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["kpi_perf"] = ft.Text("0%", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["kpi_delivery"] = ft.Text("0%", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["kpi_threats"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=RED_600)
        self.refs["kpi_sec_tag"] = ft.Text(self.t("healthy"), size=10,
                                           weight=ft.FontWeight.BOLD, color="#0b7a45")
        self.refs["kpi_sec_tag_box"] = ft.Container(
            content=self.refs["kpi_sec_tag"], bgcolor="#e5f6ee",
            padding=ft.padding.symmetric(horizontal=10, vertical=4), border_radius=99,
        )

        def kpi_card(label, value_ctrl, sub, tag_box, accent=False):
            return ft.Container(
                content=ft.Column([
                    ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color=MUTED),
                    value_ctrl,
                    ft.Text(sub, size=11, color=MUTED),
                    tag_box,
                ], spacing=4),
                padding=18, bgcolor=WHITE, border_radius=16,
                border=ft.border.all(1, LINE),
                shadow=ft.BoxShadow(blur_radius=8, color="rgba(11,26,51,0.06)"),
            )

        kpi_perf_tag = ft.Container(
            content=ft.Text("99.9%", size=10, weight=ft.FontWeight.BOLD, color=BLUE_700),
            bgcolor=BLUE_100, padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=99,
        )
        self.refs["kpi_perf_tag"] = kpi_perf_tag

        kpi_delivery_tag = ft.Container(
            content=ft.Text("0 / 0", size=10, weight=ft.FontWeight.BOLD, color=BLUE_700),
            bgcolor=BLUE_100, padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=99,
        )
        self.refs["kpi_delivery_tag"] = kpi_delivery_tag

        kpi_blocked_tag = ft.Container(
            content=ft.Text("0", size=10, weight=ft.FontWeight.BOLD, color=RED_700),
            bgcolor=RED_100, padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=99,
        )
        self.refs["kpi_blocked_tag"] = kpi_blocked_tag

        kpis = ft.ResponsiveRow([
            ft.Container(kpi_card(self.t("security_score"), self.refs["kpi_security"],
                                  self.t("sys_status"), self.refs["kpi_sec_tag_box"]),
                         col={"sm": 12, "md": 6, "lg": 3}),
            ft.Container(kpi_card(self.t("performance_score"), self.refs["kpi_perf"],
                                  self.t("uptime"), kpi_perf_tag),
                         col={"sm": 12, "md": 6, "lg": 3}),
            ft.Container(kpi_card(self.t("delivery_rate"), self.refs["kpi_delivery"],
                                  self.t("packages"), kpi_delivery_tag),
                         col={"sm": 12, "md": 6, "lg": 3}),
            ft.Container(kpi_card(self.t("active_threats"), self.refs["kpi_threats"],
                                  self.t("threats_blocked"), kpi_blocked_tag),
                         col={"sm": 12, "md": 6, "lg": 3}),
        ], spacing=14, run_spacing=14)

        # Gauges
        self.refs["gauge_dash_sec_ring"] = None
        gauge_sec = self._gauge("dash_sec", 0, BLUE_600)
        gauge_perf = self._gauge("dash_perf", 0, BLUE_600)

        gauges = ft.Row([
            ft.Container(content=ft.Column([
                gauge_sec,
                ft.Text(self.t("security_score"), size=11, weight=ft.FontWeight.BOLD,
                        color=MUTED, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=18, bgcolor=WHITE, border_radius=16, border=ft.border.all(1, LINE),
                expand=True),
            ft.Container(content=ft.Column([
                gauge_perf,
                ft.Text(self.t("performance_score"), size=11, weight=ft.FontWeight.BOLD,
                        color=MUTED, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=18, bgcolor=WHITE, border_radius=16, border=ft.border.all(1, LINE),
                expand=True),
        ], spacing=14)

        # Chart container (se actualizará periódicamente)
        self.refs["chart_dash_container"] = ft.Container(
            content=self._sparkline(self.history["cpu"], BLUE_600),
            bgcolor=WHITE, padding=18, border_radius=16, border=ft.border.all(1, LINE),
        )

        chart_block = ft.Container(
            content=ft.Column([
                ft.Text(self.t("performance_sub"), size=13, weight=ft.FontWeight.BOLD, color=BLUE_800),
                self.refs["chart_dash_container"],
            ], spacing=10),
            bgcolor=WHITE, padding=18, border_radius=16, border=ft.border.all(1, LINE),
        )

        return ft.Column([
            ft.Text(self.t("dash_title"), size=22, weight=ft.FontWeight.BOLD, color=BLUE_800),
            ft.Text(self.t("dash_sub"), size=12, color=MUTED),
            ft.Container(height=10),
            kpis,
            ft.Container(height=10),
            gauges,
            ft.Container(height=10),
            chart_block,
        ], spacing=6)

    # ========================================================
    #  VISTA: SECURITY
    # ========================================================
    def _build_security(self):
        self.refs["sec_blocked"] = ft.Text(str(self.security["blocked"]),
                                            size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["last_scan"] = ft.Text("—", size=11, color=MUTED)
        self.refs["scan_status"] = ft.Text(self.t("last_scan"), size=11, color=MUTED)
        self.refs["scan_bar"] = ft.ProgressBar(value=0, color=RED_500, bgcolor=RED_100, height=9)
        self.refs["scan_btn_label"] = ft.Text(self.t("run_scan"), size=13, color=WHITE,
                                                weight=ft.FontWeight.BOLD)

        scan_btn = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.RADAR, color=WHITE, size=16),
                self.refs["scan_btn_label"],
            ], spacing=6, tight=True),
            style=ft.ButtonStyle(bgcolor=RED_600, color=WHITE,
                                 padding=ft.padding.symmetric(horizontal=18, vertical=12),
                                 shape=ft.RoundedRectangleBorder(radius=11)),
            on_click=self._on_scan,
        )

        # Switches
        def switch_row(label, sublabel_ref, switch):
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Text(label[:3].upper(), size=11, weight=ft.FontWeight.BOLD,
                                        color=BLUE_700),
                        width=36, height=36, bgcolor=BLUE_100, border_radius=11,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column([
                        ft.Text(label, size=13, weight=ft.FontWeight.BOLD, color=INK),
                        sublabel_ref,
                    ], spacing=2, expand=True),
                    switch,
                ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(vertical=10),
                border=ft.border.only(bottom=ft.BorderSide(1, LINE)),
            )

        self.refs["fw_state"] = ft.Text(self.t("enabled"), size=11, color=MUTED)
        self.refs["enc_state"] = ft.Text(self.t("enabled"), size=11, color=MUTED)
        self.refs["auth_state"] = ft.Text(self.t("enabled"), size=11, color=MUTED)

        sw_fw = ft.Switch(value=self.security["firewall"], on_change=lambda e: self._on_switch("firewall", e))
        sw_enc = ft.Switch(value=self.security["encryption"], on_change=lambda e: self._on_switch("encryption", e))
        sw_auth = ft.Switch(value=self.security["auth"], on_change=lambda e: self._on_switch("auth", e))

        switches = ft.Column([
            switch_row(self.t("firewall"), self.refs["fw_state"], sw_fw),
            switch_row(self.t("encryption"), self.refs["enc_state"], sw_enc),
            switch_row(self.t("auth"), self.refs["auth_state"], sw_auth),
        ], spacing=4)

        self.refs["threat_list"] = ft.Column([], spacing=4)

        return ft.Column([
            ft.Text(self.t("security_title"), size=22, weight=ft.FontWeight.BOLD, color=BLUE_800),
            ft.Text(self.t("security_sub"), size=12, color=MUTED),
            ft.Container(height=10),
            ft.Row([
                ft.Container(content=ft.Column([
                    ft.Text(self.t("threats_blocked"), size=11, weight=ft.FontWeight.BOLD, color=MUTED),
                    self.refs["sec_blocked"],
                    ft.Row([ft.Text(self.t("last_scan") + ":", size=11, color=MUTED),
                            self.refs["last_scan"]], spacing=4),
                ], spacing=4), padding=18, bgcolor=WHITE, border_radius=16,
                    border=ft.border.all(1, LINE), expand=True),
                ft.Container(content=ft.Column([
                    ft.Text(self.t("run_scan"), size=11, weight=ft.FontWeight.BOLD, color=MUTED),
                    scan_btn,
                    self.refs["scan_bar"],
                    self.refs["scan_status"],
                ], spacing=10), padding=18, bgcolor=WHITE, border_radius=16,
                    border=ft.border.all(1, LINE), expand=True),
            ], spacing=14),
            ft.Container(height=14),
            ft.Row([
                ft.Container(content=ft.Column([
                    ft.Text(self.t("security_title"), size=13, weight=ft.FontWeight.BOLD, color=BLUE_800),
                    switches,
                ], spacing=8), padding=18, bgcolor=WHITE, border_radius=16,
                    border=ft.border.all(1, LINE), expand=True),
                ft.Container(content=ft.Column([
                    ft.Text(self.t("active_threats"), size=13, weight=ft.FontWeight.BOLD, color=RED_700),
                    self.refs["threat_list"],
                ], spacing=8), padding=18, bgcolor=WHITE, border_radius=16,
                    border=ft.border.all(1, LINE), expand=True),
            ], spacing=14),
        ], spacing=6)

    def _on_switch(self, key, e):
        self.security[key] = e.control.value
        self._update_switch_labels()
        self._update_metrics()

    def _update_switch_labels(self):
        for key, ref_key in [("firewall", "fw_state"), ("encryption", "enc_state"), ("auth", "auth_state")]:
            if ref_key in self.refs:
                self.refs[ref_key].value = self.t("enabled") if self.security[key] else self.t("disabled")
        self.page.update()

    def _on_scan(self, e):
        if self.scanning:
            return
        self.scanning = True
        self.refs["scan_btn_label"].value = self.t("scanning")
        self.refs["scan_status"].value = self.t("scanning")
        self.page.update()

        def _do():
            prog = 0
            while prog < 100:
                prog += random.randint(6, 16)
                self.refs["scan_bar"].value = min(prog, 100) / 100
                try:
                    self.page.update()
                except Exception:
                    return
                time.sleep(0.18)
            self.security["threats"] = max(0, self.security["threats"] - 1)
            self.security["blocked"] += random.randint(1, 5)
            self.refs["last_scan"].value = time.strftime("%H:%M:%S")
            self.refs["scan_status"].value = self.t("scan_done")
            self.refs["scan_btn_label"].value = self.t("run_scan")
            self._render_threats()
            self._update_metrics()
            time.sleep(0.9)
            self.refs["scan_bar"].value = 0
            self.scanning = False
            try:
                self.page.update()
            except Exception:
                pass

        threading.Thread(target=_do, daemon=True).start()

    def _render_threats(self):
        col = self.refs.get("threat_list")
        if col is None:
            return
        items = []
        if self.security["threats"] == 0:
            items.append(ft.Container(
                content=ft.Row([
                    ft.Container(content=ft.Icon(ft.Icons.CHECK, color="#0b7a45", size=18),
                                 width=36, height=36, bgcolor="#e5f6ee", border_radius=11,
                                 alignment=ft.alignment.center),
                    ft.Column([
                        ft.Text(self.t("healthy"), size=12, weight=ft.FontWeight.BOLD, color=INK),
                        ft.Text(f"{self.t('threats_blocked')}: {self.security['blocked']:,}",
                                size=10, color=MUTED),
                    ], spacing=0),
                ], spacing=10),
                padding=ft.padding.symmetric(vertical=8),
            ))
        else:
            for i in range(self.security["threats"]):
                name = THREAT_POOL[i % len(THREAT_POOL)]
                items.append(ft.Container(
                    content=ft.Row([
                        ft.Container(content=ft.Text("!", size=16, weight=ft.FontWeight.BOLD,
                                                      color=RED_700),
                                     width=36, height=36, bgcolor=RED_100, border_radius=11,
                                     alignment=ft.alignment.center),
                        ft.Column([
                            ft.Text(name, size=12, weight=ft.FontWeight.BOLD, color=INK),
                            ft.Text(self.t("active_threats"), size=10, color=MUTED),
                        ], spacing=0, expand=True),
                        ft.Container(
                            content=ft.Text(self.t("critical"), size=10,
                                            weight=ft.FontWeight.BOLD, color=RED_700),
                            bgcolor=RED_100,
                            padding=ft.padding.symmetric(horizontal=8, vertical=3),
                            border_radius=99,
                        ),
                    ], spacing=10),
                    padding=ft.padding.symmetric(vertical=8),
                    border=ft.border.only(bottom=ft.BorderSide(1, LINE)),
                ))
        col.controls = items
        try:
            self.page.update()
        except Exception:
            pass

    # ========================================================
    #  VISTA: PERFORMANCE
    # ========================================================
    def _build_performance(self):
        gauge_cpu = self._gauge("perf_cpu", 0, BLUE_600)
        gauge_mem = self._gauge("perf_mem", 0, BLUE_600)
        gauge_net = self._gauge("perf_net", 0, BLUE_600)

        def gauge_box(inner, label):
            return ft.Container(content=ft.Column([
                inner,
                ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color=MUTED),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=18, bgcolor=WHITE, border_radius=16, border=ft.border.all(1, LINE),
                expand=True)

        self.refs["latency"] = ft.Text("0 ms", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["uptime"] = ft.Text("0%", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["rps"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)

        def stat_card(label, ref):
            return ft.Container(content=ft.Column([
                ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color=MUTED),
                ref,
            ], spacing=4), padding=18, bgcolor=WHITE, border_radius=16,
                border=ft.border.all(1, LINE), expand=True)

        self.refs["chart_perf_container"] = ft.Container(
            content=self._sparkline(self.history["mem"], RED_600),
            bgcolor=WHITE, padding=18, border_radius=16, border=ft.border.all(1, LINE),
        )

        chart_block = ft.Container(
            content=ft.Column([
                ft.Text(self.t("performance_sub"), size=13, weight=ft.FontWeight.BOLD, color=BLUE_800),
                self.refs["chart_perf_container"],
            ], spacing=10),
            bgcolor=WHITE, padding=18, border_radius=16, border=ft.border.all(1, LINE),
        )

        return ft.Column([
            ft.Text(self.t("performance_title"), size=22, weight=ft.FontWeight.BOLD, color=BLUE_800),
            ft.Text(self.t("performance_sub"), size=12, color=MUTED),
            ft.Container(height=10),
            ft.Row([
                gauge_box(gauge_cpu, self.t("cpu")),
                gauge_box(gauge_mem, self.t("memory")),
                gauge_box(gauge_net, self.t("network")),
            ], spacing=14),
            ft.Container(height=10),
            chart_block,
            ft.Container(height=10),
            ft.Row([
                stat_card(self.t("latency"), self.refs["latency"]),
                stat_card(self.t("uptime"), self.refs["uptime"]),
                stat_card(self.t("requests"), self.refs["rps"]),
            ], spacing=14),
        ], spacing=6)

    # ========================================================
    #  VISTA: DELIVERY
    # ========================================================
    def _build_delivery(self):
        self.refs["d_total"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["d_transit"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["d_delivered"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=BLUE_800)
        self.refs["d_pending"] = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=RED_600)
        self.refs["pkg_list"] = ft.Column([], spacing=8)

        def stat_box(label, ref):
            return ft.Container(content=ft.Column([
                ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color=MUTED),
                ref,
            ], spacing=4), padding=18, bgcolor=WHITE, border_radius=16,
                border=ft.border.all(1, LINE), expand=True)

        self._render_packages()

        return ft.Column([
            ft.Text(self.t("delivery_title"), size=22, weight=ft.FontWeight.BOLD, color=BLUE_800),
            ft.Text(self.t("delivery_sub"), size=12, color=MUTED),
            ft.Container(height=10),
            ft.Row([
                stat_box(self.t("packages"), self.refs["d_total"]),
                stat_box(self.t("in_transit"), self.refs["d_transit"]),
                stat_box(self.t("delivered"), self.refs["d_delivered"]),
                stat_box(self.t("pending"), self.refs["d_pending"]),
            ], spacing=14),
            ft.Container(height=14),
            ft.Container(content=ft.Column([
                ft.Text(self.t("delivery_sub"), size=13, weight=ft.FontWeight.BOLD, color=BLUE_800),
                self.refs["pkg_list"],
            ], spacing=10), padding=18, bgcolor=WHITE, border_radius=16,
                border=ft.border.all(1, LINE)),
        ], spacing=6)

    def _render_packages(self):
        total = len(self.packages)
        delivered = sum(1 for p in self.packages if p["progress"] >= 100)
        pending = sum(1 for p in self.packages if p["progress"] == 0)
        transit = total - delivered - pending

        for k, v in [("d_total", total), ("d_transit", transit),
                     ("d_delivered", delivered), ("d_pending", pending)]:
            if k in self.refs:
                self.refs[k].value = str(v)

        if "pkg_list" not in self.refs:
            return

        items = []
        for p in self.packages:
            if p["progress"] >= 100:
                status, color, bg = self.t("delivered"), "#0b7a45", "#e5f6ee"
            elif p["progress"] == 0:
                status, color, bg = self.t("pending"), RED_700, RED_100
            else:
                status, color, bg = self.t("in_transit"), BLUE_700, BLUE_100

            items.append(ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text(p["id"], size=13, weight=ft.FontWeight.BOLD, color=BLUE_800),
                            ft.Text(f"{self.t('tracking_id')} · {p['dest']}", size=10, color=MUTED),
                        ], spacing=2, expand=True),
                        ft.Container(content=ft.Text(status, size=10, weight=ft.FontWeight.BOLD,
                                                      color=color),
                                     bgcolor=bg, padding=ft.padding.symmetric(horizontal=8, vertical=3),
                                     border_radius=99),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ProgressBar(value=p["progress"] / 100, color=BLUE_600, bgcolor=BLUE_100, height=8),
                ], spacing=8),
                padding=12, bgcolor=BLUE_50, border_radius=13,
                border=ft.border.all(1, LINE),
            ))
        self.refs["pkg_list"].controls = items

    # ========================================================
    #  VISTA: SETTINGS
    # ========================================================
    def _build_settings(self):
        lang_dd = ft.Dropdown(
            options=[ft.dropdown.Option(code, name) for code, name in LANGS],
            value=self.lang, width=200, text_size=13,
            on_change=self._change_lang, border_color=BLUE_100,
            fill_color=BLUE_100, filled=True, border_radius=9,
        )

        def setting_row(label, desc, control):
            return ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(label, size=13, weight=ft.FontWeight.BOLD, color=INK),
                        ft.Text(desc, size=11, color=MUTED),
                    ], spacing=2, expand=True),
                    control,
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(vertical=12),
                border=ft.border.only(bottom=ft.BorderSide(1, LINE)),
            )

        self.refs["saved_msg"] = ft.Text(self.t("saved"), size=12, color="#0f9d58",
                                          weight=ft.FontWeight.BOLD, visible=False)

        save_btn = ft.ElevatedButton(
            content=ft.Text(self.t("save"), color=WHITE, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(bgcolor=BLUE_700,
                                 padding=ft.padding.symmetric(horizontal=22, vertical=12),
                                 shape=ft.RoundedRectangleBorder(radius=11)),
            on_click=self._on_save,
        )

        left = ft.Container(content=ft.Column([
            setting_row(self.t("language"), "10 languages available", lang_dd),
            setting_row(self.t("notifications"), self.t("live"), ft.Switch(value=True)),
            setting_row(self.t("auto_scan"), self.t("security_sub"), ft.Switch(value=True)),
            ft.Row([save_btn, self.refs["saved_msg"]], spacing=12),
        ], spacing=4), padding=18, bgcolor=WHITE, border_radius=16,
            border=ft.border.all(1, LINE), expand=True)

        self.refs["set_threats"] = ft.Text(str(self.security["threats"]), size=10, color=MUTED)

        def info_row(icon_char, title, sub, tag_text, tag_color, tag_bg, icon_bg=BLUE_100, icon_color=BLUE_700):
            return ft.Container(content=ft.Row([
                ft.Container(content=ft.Text(icon_char, size=13, weight=ft.FontWeight.BOLD,
                                              color=icon_color),
                             width=36, height=36, bgcolor=icon_bg, border_radius=11,
                             alignment=ft.alignment.center),
                ft.Column([
                    ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color=INK),
                    ft.Text(sub, size=11, color=MUTED),
                ], spacing=2, expand=True),
                ft.Container(content=ft.Text(tag_text, size=10, weight=ft.FontWeight.BOLD,
                                              color=tag_color),
                             bgcolor=tag_bg, padding=ft.padding.symmetric(horizontal=8, vertical=3),
                             border_radius=99),
            ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(vertical=10),
                border=ft.border.only(bottom=ft.BorderSide(1, LINE)))

        right = ft.Container(content=ft.Column([
            ft.Text(self.t("sys_status"), size=11, weight=ft.FontWeight.BOLD, color=MUTED),
            info_row("✓", "Chymelix Core", "v2.4.1", self.t("healthy"), "#0b7a45", "#e5f6ee",
                     "#e5f6ee", "#0b7a45"),
            info_row("DB", "Local Node", "127.0.0.1:8443", self.t("enabled"), BLUE_700, BLUE_100),
            info_row("!", self.t("active_threats"), "", self.t("critical"), RED_700, RED_100,
                     RED_100, RED_700),
        ], spacing=4), padding=18, bgcolor=WHITE, border_radius=16,
            border=ft.border.all(1, LINE), expand=True)

        return ft.Column([
            ft.Text(self.t("settings_title"), size=22, weight=ft.FontWeight.BOLD, color=BLUE_800),
            ft.Container(height=10),
            ft.Row([left, right], spacing=14),
        ], spacing=6)

    def _on_save(self, e):
        self.refs["saved_msg"].visible = True
        self.page.update()
        def _hide():
            time.sleep(2)
            try:
                self.refs["saved_msg"].visible = False
                self.page.update()
            except Exception:
                pass
        threading.Thread(target=_hide, daemon=True).start()

    # ========================================================
    #  LOOPS DE ACTUALIZACIÓN
    # ========================================================
    def _start_loops(self):
        threading.Thread(target=self._loop_clock, daemon=True).start()
        threading.Thread(target=self._loop_metrics, daemon=True).start()
        threading.Thread(target=self._loop_packages, daemon=True).start()

    def _loop_clock(self):
        while True:
            time.sleep(1)
            try:
                if hasattr(self, "clock_text"):
                    self.clock_text.value = time.strftime("%H:%M:%S")
                    self.page.update()
            except Exception:
                return

    def _loop_metrics(self):
        while True:
            time.sleep(1.5)
            try:
                self._update_metrics()
                self.page.update()
            except Exception:
                return

    def _loop_packages(self):
        while True:
            time.sleep(2.6)
            try:
                for p in self.packages:
                    if p["progress"] < 100:
                        p["progress"] = min(100, p["progress"] + random.randint(1, 9))
                self._render_packages()
                self._update_kpi_delivery()
                self.page.update()
            except Exception:
                return

    # -------- cálculo de métricas --------
    def _update_metrics(self):
        p = self.perf

        p["cpu"] = max(8.0, min(92.0, p["cpu"] + random.uniform(-6, 6)))
        p["mem"] = max(25.0, min(90.0, p["mem"] + random.uniform(-3.5, 3.5)))
        p["net"] = max(10.0, min(95.0, p["net"] + random.uniform(-7, 7)))
        p["latency"] = max(6.0, min(90.0, p["latency"] + random.uniform(-4, 4)))
        p["rps"] = int(max(400, min(3200, p["rps"] + random.uniform(-140, 140))))
        p["uptime"] = max(99.7, min(100.0, p["uptime"] + random.uniform(-0.01, 0.012)))

        self.history["cpu"].append(p["cpu"])
        self.history["mem"].append(p["mem"])
        if len(self.history["cpu"]) > 40: self.history["cpu"].pop(0)
        if len(self.history["mem"]) > 40: self.history["mem"].pop(0)

        sec_score = self._compute_security_score()
        perf_score = self._compute_perf_score()

        # KPIs dashboard
        if "kpi_security" in self.refs:
            self.refs["kpi_security"].value = f"{int(sec_score)}%"
        if "kpi_perf" in self.refs:
            self.refs["kpi_perf"].value = f"{int(perf_score)}%"
        if "kpi_threats" in self.refs:
            self.refs["kpi_threats"].value = str(self.security["threats"])
        if "kpi_sec_tag" in self.refs:
            if sec_score >= 85:
                self.refs["kpi_sec_tag"].value = self.t("healthy")
                self.refs["kpi_sec_tag"].color = "#0b7a45"
                self.refs["kpi_sec_tag_box"].bgcolor = "#e5f6ee"
            elif sec_score >= 60:
                self.refs["kpi_sec_tag"].value = self.t("warning")
                self.refs["kpi_sec_tag"].color = BLUE_700
                self.refs["kpi_sec_tag_box"].bgcolor = BLUE_100
            else:
                self.refs["kpi_sec_tag"].value = self.t("critical")
                self.refs["kpi_sec_tag"].color = RED_700
                self.refs["kpi_sec_tag_box"].bgcolor = RED_100
        if "kpi_perf_tag" in self.refs:
            self.refs["kpi_perf_tag"].content.value = f"{p['uptime']:.2f}%"
        if "kpi_blocked_tag" in self.refs:
            self.refs["kpi_blocked_tag"].content.value = f"{self.security['blocked']:,}"

        # Gauges dashboard
        self._set_gauge("dash_sec", sec_score)
        self._set_gauge("dash_perf", perf_score)

        # Gauges performance
        self._set_gauge("perf_cpu", p["cpu"])
        self._set_gauge("perf_mem", p["mem"])
        self._set_gauge("perf_net", p["net"])

        # Métricas texto performance
        if "latency" in self.refs:
            self.refs["latency"].value = f"{int(p['latency'])} ms"
        if "uptime" in self.refs:
            self.refs["uptime"].value = f"{p['uptime']:.2f}%"
        if "rps" in self.refs:
            self.refs["rps"].value = f"{p['rps']:,}"

        # Charts
        if "chart_dash_container" in self.refs:
            self.refs["chart_dash_container"].content = self._sparkline(self.history["cpu"], BLUE_600)
        if "chart_perf_container" in self.refs:
            self.refs["chart_perf_container"].content = self._sparkline(self.history["mem"], RED_600)

        # Security view refs
        if "sec_blocked" in self.refs:
            self.refs["sec_blocked"].value = f"{self.security['blocked']:,}"

    def _set_gauge(self, key, pct):
        ring = self.refs.get(f"gauge_{key}_ring")
        num = self.refs.get(f"gauge_{key}_num")
        if ring is not None:
            ring.value = pct / 100
            if pct < 60:
                ring.color = RED_600
            else:
                ring.color = BLUE_600
        if num is not None:
            num.value = f"{int(pct)}%"

    def _update_kpi_delivery(self):
        total = len(self.packages)
        delivered = sum(1 for p in self.packages if p["progress"] >= 100)
        rate = (delivered / total * 100) if total else 0
        if "kpi_delivery" in self.refs:
            self.refs["kpi_delivery"].value = f"{int(rate)}%"
        if "kpi_delivery_tag" in self.refs:
            self.refs["kpi_delivery_tag"].content.value = f"{delivered} / {total}"

    def _compute_security_score(self):
        s = 100
        if not self.security["firewall"]: s -= 30
        if not self.security["encryption"]: s -= 30
        if not self.security["auth"]: s -= 25
        s -= self.security["threats"] * 8
        return max(0.0, min(100.0, s))

    def _compute_perf_score(self):
        p = self.perf
        load = p["cpu"] * 0.4 + p["mem"] * 0.35 + p["net"] * 0.25
        return max(0.0, min(100.0, 100 - (load - 35) * 0.85))


# ============================================================
#  MAIN
# ============================================================
def main(page: ft.Page):
    ChymelixApp(page)
    # Refrescar primeras métricas y amenazas
    app = None  # placeholder


if __name__ == "__main__":
    ft.app(target=main)
