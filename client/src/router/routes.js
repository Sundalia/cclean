const routes = [
  {
    path: '/',
    component: () => import('layouts/SiteLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Site/IndexPage.vue') },
      { path: 'spring_cleaning', component: () => import('pages/Site/SpringPage.vue') },
      { path: 'maintenance_cleaning', component:() => import('pages/Site/MaintenancePage.vue') },
      { path: 'window_cleaning', component: () => import('pages/Site/WindowPage.vue') },
      { path: 'post_construction_cleaning', component: () => import('pages/Site/PostConstructionPage.vue') },
      { path: 'industrial_cleaning', component: () => import('pages/Site/IndustrialPage.vue') },
      { path: 'office_cleaning',  component: () => import('pages/Site/OfficePage.vue') },
      { path: 'cottage_cleaning',  component: () => import('pages/Site/CottagePage.vue') },
      { path: 'yacht', component: () => import('pages/Site/YachtPage.vue') },
      { path: 'rotor', component: () => import('pages/Site/RotorPage.vue') },
      { path: 'portfolio', component: () => import('pages/Site/PortfolioPage.vue') },
      { path: 'contact_us', component: () => import('pages/Site/ContactPage.vue') },
      { path: 'vacancies', component: () => import('pages/Site/VacanciesPage.vue') },
      { path: 'documents', component: () => import('pages/Site/DocumentsPage.vue') },     
    ],
  },
  {
    path: '/account',
    component: () => import('layouts/AccountLayout.vue'),
    children: [
      { path: 'order', component: () =>import('pages/Account/OrderPage.vue') }
    ],
  },
  // {
  //   path:'/auth',
  //   component: () => import('layouts/EmptyLayout.vue'),
  //   children: [
  //     { path: 'auth', component: () => import('pages/Empty/AuthenticationPage.vue') },
  //   ]
  // },

  // Always leave this as last one,
  // but you can also remove it
  
  {
     path: '/:catchAll(.*)*', component: () => import('../pages/Empty/NotFoundPage.vue')
  }
]

export default routes
