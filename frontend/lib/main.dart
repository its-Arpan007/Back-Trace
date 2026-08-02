import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/theme/app_theme.dart';
import 'package:backtrace/routes/app_router.dart';
import 'package:backtrace/utils/logger.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  AppLogger.i('Initializing BACKTRACE Application Foundation...');
  runApp(
    const ProviderScope(
      child: BacktraceApp(),
    ),
  );
}

class BacktraceApp extends StatelessWidget {
  const BacktraceApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'BACKTRACE - Learning Intelligence Platform',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.dark,
      routerConfig: appRouter,
    );
  }
}
