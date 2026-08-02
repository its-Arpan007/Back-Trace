import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/routes/route_paths.dart';
import 'package:backtrace/features/splash/presentation/views/splash_screen.dart';
import 'package:backtrace/features/auth/presentation/views/welcome_screen.dart';
import 'package:backtrace/features/auth/presentation/views/login_screen.dart';
import 'package:backtrace/features/auth/presentation/views/register_screen.dart';
import 'package:backtrace/features/auth/presentation/views/forgot_password_screen.dart';
import 'package:backtrace/features/auth/presentation/views/reset_password_screen.dart';
import 'package:backtrace/features/auth/presentation/views/email_verification_screen.dart';
import 'package:backtrace/features/auth/presentation/views/complete_profile_screen.dart';
import 'package:backtrace/features/profile/presentation/views/profile_screen.dart';
import 'package:backtrace/features/profile/presentation/views/settings_screen.dart';
import 'package:backtrace/features/profile/presentation/views/account_security_screen.dart';

import 'package:backtrace/features/curriculum/presentation/views/subject_explorer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/chapter_explorer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/topic_explorer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/concept_explorer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/concept_details_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/knowledge_graph_viewer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/learning_path_viewer_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/curriculum_search_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/curriculum_import_status_screen.dart';
import 'package:backtrace/features/curriculum/presentation/views/graph_validation_report_screen.dart';

import 'package:backtrace/features/question/presentation/views/question_explorer_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_details_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_editor_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_preview_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_import_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_validation_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_statistics_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_search_screen.dart';
import 'package:backtrace/features/question/presentation/views/question_version_history_screen.dart';
import 'package:backtrace/features/question/presentation/views/adaptive_practice_generator_screen.dart';

import 'package:backtrace/features/diagnosis/presentation/views/answer_submission_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/evaluation_summary_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/diagnosis_report_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/evidence_viewer_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/weak_concept_viewer_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/misconception_viewer_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/learning_impact_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/recommended_actions_screen.dart';
import 'package:backtrace/features/diagnosis/presentation/views/diagnosis_history_screen.dart';

import 'package:backtrace/features/mastery/presentation/views/student_knowledge_map_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/mastery_dashboard_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/concept_timeline_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/learning_progress_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/retention_dashboard_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/knowledge_decay_view_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/learning_velocity_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/confidence_dashboard_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/study_history_screen.dart';
import 'package:backtrace/features/mastery/presentation/views/goal_tracker_screen.dart';

import 'package:backtrace/features/recommendation/presentation/views/recommendation_dashboard_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/todays_learning_plan_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/weekly_learning_plan_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/recommended_questions_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/recommended_resources_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/revision_queue_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/review_schedule_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/goal_dashboard_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/adaptive_learning_path_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/recommendation_history_screen.dart';
import 'package:backtrace/features/recommendation/presentation/views/recommendation_feedback_screen.dart';

import 'package:backtrace/features/analytics/presentation/views/analytics_dashboard_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/student_progress_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/learning_heatmap_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/concept_analytics_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/question_analytics_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/recommendation_analytics_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/prediction_dashboard_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/performance_reports_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/weekly_summary_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/monthly_summary_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/teacher_insights_screen.dart';
import 'package:backtrace/features/analytics/presentation/views/institution_dashboard_screen.dart';

import 'package:backtrace/features/student_dashboard/presentation/views/student_home_dashboard_screen.dart';
import 'package:backtrace/features/learning_session/presentation/views/session_launcher_screen.dart';
import 'package:backtrace/features/question_player/presentation/views/question_player_screen.dart';
import 'package:backtrace/features/reflection/presentation/views/reflection_screen.dart';
import 'package:backtrace/features/knowledge_map/presentation/views/interactive_knowledge_map_screen.dart';
import 'package:backtrace/features/progress/presentation/views/student_progress_dashboard_screen.dart';
import 'package:backtrace/features/goals/presentation/views/student_goals_screen.dart';
import 'package:backtrace/features/notifications/presentation/views/notifications_screen.dart';
import 'package:backtrace/features/profile/presentation/views/student_profile_screen.dart';
import 'package:backtrace/features/settings/presentation/views/app_settings_screen.dart';

import 'package:backtrace/features/teacher_dashboard/presentation/views/teacher_dashboard_screen.dart';
import 'package:backtrace/features/class_management/presentation/views/class_management_screen.dart';
import 'package:backtrace/features/student_profile/presentation/views/teacher_student_profile_screen.dart';
import 'package:backtrace/features/assessment_builder/presentation/views/assessment_builder_screen.dart';
import 'package:backtrace/features/assignments/presentation/views/assignment_management_screen.dart';
import 'package:backtrace/features/interventions/presentation/views/intervention_center_screen.dart';
import 'package:backtrace/features/reports/presentation/views/teacher_reports_screen.dart';

import 'package:backtrace/features/admin_dashboard/presentation/views/admin_dashboard_screen.dart';
import 'package:backtrace/features/user_management/presentation/views/admin_user_management_screen.dart';
import 'package:backtrace/features/curriculum_management/presentation/views/admin_curriculum_management_screen.dart';
import 'package:backtrace/features/knowledge_graph_editor/presentation/views/admin_knowledge_graph_editor_screen.dart';
import 'package:backtrace/features/question_bank/presentation/views/admin_question_bank_screen.dart';
import 'package:backtrace/features/resource_management/presentation/views/admin_resource_management_screen.dart';
import 'package:backtrace/features/ai_config/presentation/views/admin_ai_config_screen.dart';
import 'package:backtrace/features/system_monitoring/presentation/views/admin_system_monitoring_screen.dart';
import 'package:backtrace/features/audit_center/presentation/views/admin_audit_center_screen.dart';
import 'package:backtrace/features/approval_center/presentation/views/admin_approval_center_screen.dart';
import 'package:backtrace/features/backup_restore/presentation/views/admin_backup_restore_screen.dart';

import 'package:backtrace/features/ai_chat/presentation/views/ai_chat_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/ai_study_coach_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/ai_teacher_assistant_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/ai_admin_assistant_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/concept_explainer_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/ai_study_planner_screen.dart';
import 'package:backtrace/features/ai_chat/presentation/views/ai_reflection_coach_screen.dart';

final appRouter = GoRouter(
  initialLocation: RoutePaths.splash,
  routes: [
    GoRoute(
      path: RoutePaths.splash,
      builder: (context, state) => const SplashScreen(),
    ),
    GoRoute(
      path: '/welcome',
      builder: (context, state) => const WelcomeScreen(),
    ),
    GoRoute(
      path: '/login',
      builder: (context, state) => const LoginScreen(),
    ),
    GoRoute(
      path: '/register',
      builder: (context, state) => const RegisterScreen(),
    ),
    GoRoute(
      path: '/forgot-password',
      builder: (context, state) => const ForgotPasswordScreen(),
    ),
    GoRoute(
      path: '/reset-password',
      builder: (context, state) => const ResetPasswordScreen(),
    ),
    GoRoute(
      path: '/email-verification',
      builder: (context, state) => const EmailVerificationScreen(),
    ),
    GoRoute(
      path: '/complete-profile',
      builder: (context, state) => const CompleteProfileScreen(),
    ),
    GoRoute(
      path: '/profile',
      builder: (context, state) => const ProfileScreen(),
    ),
    GoRoute(
      path: '/settings',
      builder: (context, state) => const SettingsScreen(),
    ),
    GoRoute(
      path: '/account-security',
      builder: (context, state) => const AccountSecurityScreen(),
    ),
    GoRoute(
      path: '/subject-explorer',
      builder: (context, state) => const SubjectExplorerScreen(),
    ),
    GoRoute(
      path: '/chapters-explorer',
      builder: (context, state) => const ChapterExplorerScreen(),
    ),
    GoRoute(
      path: '/topics-explorer',
      builder: (context, state) => const TopicExplorerScreen(),
    ),
    GoRoute(
      path: '/concepts-explorer',
      builder: (context, state) => const ConceptExplorerScreen(),
    ),
    GoRoute(
      path: '/concept-details',
      builder: (context, state) => const ConceptDetailsScreen(),
    ),
    GoRoute(
      path: '/knowledge-graph-viewer',
      builder: (context, state) => const KnowledgeGraphViewerScreen(),
    ),
    GoRoute(
      path: '/learning-path-viewer',
      builder: (context, state) => const LearningPathViewerScreen(),
    ),
    GoRoute(
      path: '/curriculum-search',
      builder: (context, state) => const CurriculumSearchScreen(),
    ),
    GoRoute(
      path: '/curriculum-import-status',
      builder: (context, state) => const CurriculumImportStatusScreen(),
    ),
    GoRoute(
      path: '/graph-validation-report',
      builder: (context, state) => const GraphValidationReportScreen(),
    ),
    GoRoute(
      path: '/question-explorer',
      builder: (context, state) => const QuestionExplorerScreen(),
    ),
    GoRoute(
      path: '/question-details',
      builder: (context, state) => const QuestionDetailsScreen(),
    ),
    GoRoute(
      path: '/question-editor',
      builder: (context, state) => const QuestionEditorScreen(),
    ),
    GoRoute(
      path: '/question-preview',
      builder: (context, state) => const QuestionPreviewScreen(),
    ),
    GoRoute(
      path: '/question-import',
      builder: (context, state) => const QuestionImportScreen(),
    ),
    GoRoute(
      path: '/question-validation',
      builder: (context, state) => const QuestionValidationScreen(),
    ),
    GoRoute(
      path: '/question-statistics',
      builder: (context, state) => const QuestionStatisticsScreen(),
    ),
    GoRoute(
      path: '/question-search',
      builder: (context, state) => const QuestionSearchScreen(),
    ),
    GoRoute(
      path: '/question-version-history',
      builder: (context, state) => const QuestionVersionHistoryScreen(),
    ),
    GoRoute(
      path: '/adaptive-practice-generator',
      builder: (context, state) => const AdaptivePracticeGeneratorScreen(),
    ),
    GoRoute(
      path: '/answer-submission',
      builder: (context, state) => const AnswerSubmissionScreen(),
    ),
    GoRoute(
      path: '/evaluation-summary',
      builder: (context, state) => const EvaluationSummaryScreen(),
    ),
    GoRoute(
      path: '/diagnosis-report',
      builder: (context, state) => const DiagnosisReportScreen(),
    ),
    GoRoute(
      path: '/evidence-viewer',
      builder: (context, state) => const EvidenceViewerScreen(),
    ),
    GoRoute(
      path: '/weak-concept-viewer',
      builder: (context, state) => const WeakConceptViewerScreen(),
    ),
    GoRoute(
      path: '/misconception-viewer',
      builder: (context, state) => const MisconceptionViewerScreen(),
    ),
    GoRoute(
      path: '/learning-impact',
      builder: (context, state) => const LearningImpactScreen(),
    ),
    GoRoute(
      path: '/recommended-actions',
      builder: (context, state) => const RecommendedActionsScreen(),
    ),
    GoRoute(
      path: '/diagnosis-history',
      builder: (context, state) => const DiagnosisHistoryScreen(),
    ),
    GoRoute(
      path: '/student-knowledge-map',
      builder: (context, state) => const StudentKnowledgeMapScreen(),
    ),
    GoRoute(
      path: '/mastery-dashboard',
      builder: (context, state) => const MasteryDashboardScreen(),
    ),
    GoRoute(
      path: '/concept-timeline',
      builder: (context, state) => const ConceptTimelineScreen(),
    ),
    GoRoute(
      path: '/learning-progress',
      builder: (context, state) => const LearningProgressScreen(),
    ),
    GoRoute(
      path: '/retention-dashboard',
      builder: (context, state) => const RetentionDashboardScreen(),
    ),
    GoRoute(
      path: '/knowledge-decay-view',
      builder: (context, state) => const KnowledgeDecayViewScreen(),
    ),
    GoRoute(
      path: '/learning-velocity',
      builder: (context, state) => const LearningVelocityScreen(),
    ),
    GoRoute(
      path: '/confidence-dashboard',
      builder: (context, state) => const ConfidenceDashboardScreen(),
    ),
    GoRoute(
      path: '/study-history',
      builder: (context, state) => const StudyHistoryScreen(),
    ),
    GoRoute(
      path: '/goal-tracker',
      builder: (context, state) => const GoalTrackerScreen(),
    ),
    GoRoute(
      path: '/recommendation-dashboard',
      builder: (context, state) => const RecommendationDashboardScreen(),
    ),
    GoRoute(
      path: '/todays-learning-plan',
      builder: (context, state) => const TodaysLearningPlanScreen(),
    ),
    GoRoute(
      path: '/weekly-learning-plan',
      builder: (context, state) => const WeeklyLearningPlanScreen(),
    ),
    GoRoute(
      path: '/recommended-questions',
      builder: (context, state) => const RecommendedQuestionsScreen(),
    ),
    GoRoute(
      path: '/recommended-resources',
      builder: (context, state) => const RecommendedResourcesScreen(),
    ),
    GoRoute(
      path: '/revision-queue',
      builder: (context, state) => const RevisionQueueScreen(),
    ),
    GoRoute(
      path: '/review-schedule',
      builder: (context, state) => const ReviewScheduleScreen(),
    ),
    GoRoute(
      path: '/goal-dashboard',
      builder: (context, state) => const GoalDashboardScreen(),
    ),
    GoRoute(
      path: '/adaptive-learning-path',
      builder: (context, state) => const AdaptiveLearningPathScreen(),
    ),
    GoRoute(
      path: '/recommendation-history',
      builder: (context, state) => const RecommendationHistoryScreen(),
    ),
    GoRoute(
      path: '/recommendation-feedback',
      builder: (context, state) => const RecommendationFeedbackScreen(),
    ),
    GoRoute(
      path: '/analytics-dashboard',
      builder: (context, state) => const AnalyticsDashboardScreen(),
    ),
    GoRoute(
      path: '/student-progress',
      builder: (context, state) => const StudentProgressScreen(),
    ),
    GoRoute(
      path: '/learning-heatmap',
      builder: (context, state) => const LearningHeatmapScreen(),
    ),
    GoRoute(
      path: '/concept-analytics',
      builder: (context, state) => const ConceptAnalyticsScreen(),
    ),
    GoRoute(
      path: '/question-analytics',
      builder: (context, state) => const QuestionAnalyticsScreen(),
    ),
    GoRoute(
      path: '/recommendation-analytics',
      builder: (context, state) => const RecommendationAnalyticsScreen(),
    ),
    GoRoute(
      path: '/prediction-dashboard',
      builder: (context, state) => const PredictionDashboardScreen(),
    ),
    GoRoute(
      path: '/performance-reports',
      builder: (context, state) => const PerformanceReportsScreen(),
    ),
    GoRoute(
      path: '/weekly-summary',
      builder: (context, state) => const WeeklySummaryScreen(),
    ),
    GoRoute(
      path: '/monthly-summary',
      builder: (context, state) => const MonthlySummaryScreen(),
    ),
    GoRoute(
      path: '/teacher-insights',
      builder: (context, state) => const TeacherInsightsScreen(),
    ),
    GoRoute(
      path: '/institution-dashboard',
      builder: (context, state) => const InstitutionDashboardScreen(),
    ),
    GoRoute(
      path: '/student-home-dashboard',
      builder: (context, state) => const StudentHomeDashboardScreen(),
    ),
    GoRoute(
      path: '/session-launcher',
      builder: (context, state) => const SessionLauncherScreen(),
    ),
    GoRoute(
      path: '/question-player',
      builder: (context, state) => const QuestionPlayerScreen(),
    ),
    GoRoute(
      path: '/reflection',
      builder: (context, state) => const ReflectionScreen(),
    ),
    GoRoute(
      path: '/interactive-knowledge-map',
      builder: (context, state) => const InteractiveKnowledgeMapScreen(),
    ),
    GoRoute(
      path: '/student-progress-dashboard',
      builder: (context, state) => const StudentProgressDashboardScreen(),
    ),
    GoRoute(
      path: '/student-goals',
      builder: (context, state) => const StudentGoalsScreen(),
    ),
    GoRoute(
      path: '/notifications',
      builder: (context, state) => const NotificationsScreen(),
    ),
    GoRoute(
      path: '/student-profile',
      builder: (context, state) => const StudentProfileScreen(),
    ),
    GoRoute(
      path: '/app-settings',
      builder: (context, state) => const AppSettingsScreen(),
    ),
    GoRoute(
      path: '/teacher-dashboard',
      builder: (context, state) => const TeacherDashboardScreen(),
    ),
    GoRoute(
      path: '/class-management',
      builder: (context, state) => const ClassManagementScreen(),
    ),
    GoRoute(
      path: '/teacher-student-profile',
      builder: (context, state) => const TeacherStudentProfileScreen(),
    ),
    GoRoute(
      path: '/assessment-builder',
      builder: (context, state) => const AssessmentBuilderScreen(),
    ),
    GoRoute(
      path: '/assignment-management',
      builder: (context, state) => const AssignmentManagementScreen(),
    ),
    GoRoute(
      path: '/intervention-center',
      builder: (context, state) => const InterventionCenterScreen(),
    ),
    GoRoute(
      path: '/teacher-reports',
      builder: (context, state) => const TeacherReportsScreen(),
    ),
    GoRoute(
      path: '/admin-dashboard',
      builder: (context, state) => const AdminDashboardScreen(),
    ),
    GoRoute(
      path: '/admin-user-management',
      builder: (context, state) => const AdminUserManagementScreen(),
    ),
    GoRoute(
      path: '/admin-curriculum-management',
      builder: (context, state) => const AdminCurriculumManagementScreen(),
    ),
    GoRoute(
      path: '/admin-knowledge-graph-editor',
      builder: (context, state) => const AdminKnowledgeGraphEditorScreen(),
    ),
    GoRoute(
      path: '/admin-question-bank',
      builder: (context, state) => const AdminQuestionBankScreen(),
    ),
    GoRoute(
      path: '/admin-resource-management',
      builder: (context, state) => const AdminResourceManagementScreen(),
    ),
    GoRoute(
      path: '/admin-ai-config',
      builder: (context, state) => const AdminAiConfigScreen(),
    ),
    GoRoute(
      path: '/admin-system-monitoring',
      builder: (context, state) => const AdminSystemMonitoringScreen(),
    ),
    GoRoute(
      path: '/admin-audit-center',
      builder: (context, state) => const AdminAuditCenterScreen(),
    ),
    GoRoute(
      path: '/admin-approval-center',
      builder: (context, state) => const AdminApprovalCenterScreen(),
    ),
    GoRoute(
      path: '/admin-backup-restore',
      builder: (context, state) => const AdminBackupRestoreScreen(),
    ),
    GoRoute(
      path: '/ai-chat',
      builder: (context, state) => const AIChatScreen(),
    ),
    GoRoute(
      path: '/ai-study-coach',
      builder: (context, state) => const AIStudyCoachScreen(),
    ),
    GoRoute(
      path: '/ai-teacher-assistant',
      builder: (context, state) => const AITeacherAssistantScreen(),
    ),
    GoRoute(
      path: '/ai-admin-assistant',
      builder: (context, state) => const AIAdminAssistantScreen(),
    ),
    GoRoute(
      path: '/concept-explainer',
      builder: (context, state) => const ConceptExplainerScreen(),
    ),
    GoRoute(
      path: '/ai-study-planner',
      builder: (context, state) => const AIStudyPlannerScreen(),
    ),
    GoRoute(
      path: '/ai-reflection-coach',
      builder: (context, state) => const AIReflectionCoachScreen(),
    ),
  ],
  errorBuilder: (context, state) => Scaffold(
    body: Center(
      child: Text('Route not found: ${state.error}'),
    ),
  ),
);
