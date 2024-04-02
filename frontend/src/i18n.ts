import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n
  .use(initReactI18next)
  .init({
    debug: true,
    fallbackLng: 'ru',
    interpolation: {
      escapeValue: false, 
    },
    resources: {
      ru: {
        translation: {
        flag: "🇷🇺",
        langCode: "ru",
        home: "Главная",
        teams: "Команды",
        myTeams: "Мои команды",
        something: "Что-то",
        LightTheme: "Светлая",
        DarkTheme: "Темная",
        SystemTheme: "Тема устройства",
        entrance: "Вход",
        login: "Авторизация",
        registration: "Регистрация",
        loginHeader: "Введите адрес электронной почты и пароль, чтобы начать.",
        regHeader: "Введите юзернейм, почту и пароль, чтобы зарегистрироваться.",
        buttonLoginInSystem: "Войти в систему",
        buttonRegInSystemStep1: "Продолжить",
        buttonGoTOReg: "Приступить к регистрации!",
        landingLogo: "Упростим подбор!",
        landingDesc: "Сделаем вашу жизнь проще! Забудьте о долгом переборе как о нудной рутине!",
        respondRequest: "Откликнуться на заявку",
        vacancy: "Вакансии",
        iorganizer: "Я организатор",
        viewingProfile: "Просмотр профиля",
        skills:"Скиллы",
        age: "Возраст",
        EditTree: "Редактировать дерево",
        DistTeams: "Распределение команд",
        distribute: "Распределить",
        download: "Скачать",
        descDownload: "Скачать XLS таблицу",
        open: "Открыть",
        

        }
      },
      en: {
        translation: {
            flag: "🇬🇧",
            langCode: "en",
            home: "Home",
            teams: "Teams",
            myTeams: "My Teams",
            Interests: "Interests",
            something: "Something",
            LightTheme: "Light",
            DarkTheme: "Dark",
            SystemTheme: "System Theme", 
            entrance: "Sign in",
            login: "Log in",
            registration: "Sign up",
            loginHeader: " Enter your email address and password to get started.",
            buttonLoginInSystem: "log in",
            buttonRegInSystemStep1: "Continue",
            buttonGoTOReg: "Proceed with registration!",
            landingLogo: "Let's simplify the selection!",
            landingDesc:"Let's make your life easier! Forget about the long search as a tedious routine!",
            respondRequest: "respond to the request",
            vacancy: "vacancy",
            iorganizer: "I'm the organizer",
            viewingProfile: "Viewing a profile",
            skills:"Skills",
            age: "Age",
            EditTree: "Edit the tree",
            DistTeams: "Distribution of teams",
            distribute: "Distribute it",
            download: "Download",
            descDownload: "Download the XLS table",
            open: "Open",

             }
      },
      zh: {
        translation: {
            flag: "🇨🇳",
            langCode: "zn",
            home: "家",
            teams: "团队",
            myTeams: "我的命令",
            something: "某物",
            LightTheme: "光",
            DarkTheme: "黑暗",
            SystemTheme: "系统主题",
            entrance: "登入您的帐户",
            login: "登录",
            registration: "登记注册",
            loginHeader: "请输入您的电子邮件地址和密码，开始更改.",
            buttonLoginInSystem: "登录系统",
            buttonRegInSystemStep1: "继续",
            buttonGoTOReg: "继续登记！",
            landingLogo: "让我们简化选择！",
            landingDesc: "让我们让你的生活更轻松！ 忘记长时间的搜索作为一个繁琐的例程！",
            respondRequest: "响应请求",
            vacancy: "职位空缺",
            iorganizer: "我是组织者",
            viewingProfile: "查看个人资料",
            skills:"技能",
            age: "年龄",
            EditTree: "编辑树",
            DistTeams: "团队分布",
            distribute: "分发它",
            download: "下载",
            descDownload: "下载XLS表",
            open: "打开",
        }
      },
    }
  });

export default i18n;